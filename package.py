name = 'libigl'

version = '2.6.0.hh.1.0.0'

authors = [
    'Libigl',
]

description = '''Geometry processing lib'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']
    c.plugins.release_hook.hh_emailer.recipients = []

requires = [
]

private_build_requires = [
]

variants = [
]

def commands():
    env.REZ_LIBIGL_ROOT = '{root}'
    env.CPATH.append('{root}/include')
    env.LIBIGL_INCLUDES = '{root}/include'
    env.LIBRARY_PATH.append('{root}/lib64')
    env.LD_LIBRARY_PATH.append('{root}/lib64')


uuid = 'repository.libigl'
