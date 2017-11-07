import os

import shutil

PYTHON_VERSIONS = [
    'py3.7-rc',
    'py3.6',
    'py3.5',
    'py3.4',
    'py2.7'
]

PANDAS_VERSIONS = [
    '0.20.3',
    '0.19.2'
]


def main():
    with open('Dockerfile.alpine') as f:
        template = f.read()

    try:
        shutil.rmtree('dockerfiles')
    except FileNotFoundError:
        pass

    for python_version in PYTHON_VERSIONS:
        for pandas_version in PANDAS_VERSIONS:
            path = 'dockerfiles/{python_version}/{pandas_version}'.format(**locals())
            os.makedirs(path, exist_ok=True)

            with open('{path}/Dockerfile'.format(**locals()), 'w') as f:
                f.write('# FILE GENERATED AUTOMATICALLY, DO NOT EDIT MANUALLY\n\n')
                f.write(template.format(**locals()))


if __name__ == '__main__':
    main()
