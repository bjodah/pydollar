"""
pydollar provides an installable import hook to support the dollar sign ($) as valid python syntax.
"""
import ast
from collections import OrderedDict
import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import io
import sys
import tokenize

__version__ = '0.1.3'


# inspiration from blog post:
# stupidpythonideas.blogspot.com/2015/06/hacking-python-without-hacking-python.html
# improved design by consulting mercurial's __init__.py


def walk_up_for_assign(node, parent_of):
    if node not in parent_of:
        return None
    parent = parent_of[node]
    if isinstance(parent, ast.Assign):
        tgt0 = parent.targets[0]
        if isinstance(tgt0, ast.Tuple):
            return tuple(name.id for name in tgt0.elts)
        elif isinstance(tgt0, ast.Name):
            return (tgt0.id)
        else:
            raise NotImplementedError("Unknown node type: %s" % tgt0)
    else:
        return walk_up_for_assign(parent, parent_of)


class SupportDollar(ast.NodeTransformer):

    literal_token = '$'

    def __init__(self, literal_name, tree, parent_of):
        self.literal_name = literal_name
        self.tree = tree
        self.parent_of = parent_of

    def visit_Name(self, node):
        if node.id == self.literal_name:
            names = walk_up_for_assign(node, self.parent_of)
            if names is None:
                raise NotImplementedError("The nodetransformer got confused :/")
            return ast.copy_location(ast.Tuple(elts=[
                ast.Str(s=name) for name in names
            ], ctx=ast.Load()), node)
        else:
            return node

    def visit_Str(self, node):
        if self.literal_name in node.s:
            s = node.s.replace(self.literal_name, self.literal_token)
            return ast.copy_location(ast.Str(s=s), node)
        else:
            return node

def my_walk(tree):
    parents = OrderedDict()
    for node in ast.iter_child_nodes(tree):
        parents[node] = tree
        parents.update(my_walk(node))  # could reach maximum recursion depth.
    return parents


class PyDollarLoader(importlib.machinery.SourceFileLoader):

    def get_data(self, path):
        data = super().get_data(path)
        if not path.endswith(tuple(importlib.machinery.BYTECODE_SUFFIXES)):
            return data

        if data[:2] != self.__class__.bytecodeheader[:2]:
            raise OSError("No PyDollar header")
        if data[:4] != self.__class__.bytecodeheader[:4]:
            raise OSError("PyDollar header version mismatch")
        return data[4:]

    def set_data(self, path, data, *args, **kwargs):
        if path.endswith(tuple(importlib.machinery.BYTECODE_SUFFIXES)):
            data = self.__class__.bytecodeheader + data
        return super().set_data(path, data, *args, **kwargs)

    def source_to_code(self, data, path, *, _optimize=-1):
        source = importlib.util.decode_source(data)
        i = 0
        while True:
            literal_name = '_DOLLAR_SIGN_LITERAL_{}_'.format(i)
            if literal_name not in source:
                break
            i += 1  # ensures that we are free of collisions

        source = source.replace(SupportDollar.literal_token, literal_name)
        tree = compile(source, path, 'exec', dont_inherit=True, optimize=_optimize,
                       flags=ast.PyCF_ONLY_AST)
        parent_of = my_walk(tree)
        tree = SupportDollar(literal_name, tree, parent_of).visit(tree)
        ast.fix_missing_locations(tree)
        return compile(tree, path, 'exec', dont_inherit=True, optimize=_optimize)


PyDollarLoader.bytecodeheader = b'PD\x00\x00'  # must be bumped when this code changes.


class PyDollarPathFinder(importlib.abc.MetaPathFinder):

    def find_spec(self, fullname, path, target=None):
        spec = None
        for finder in sys.meta_path:
            if finder == self:
                continue
            if not hasattr(finder, 'find_spec'):
                continue
            spec = finder.find_spec(fullname, path, target=target)
            if spec:
                break
        if not spec:
            return None
        spec.loader = PyDollarLoader(spec.name, spec.origin)
        return spec


def install_import_hook():
    if not any(isinstance(x, PyDollarPathFinder) for x in sys.meta_path):
        sys.meta_path.insert(0, PyDollarPathFinder())
