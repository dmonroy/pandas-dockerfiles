import os

import shutil

NUMPY_VERSIONS = [
    'py3.7-rc-1.13',
    'py3.6-1.13.3'
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

    for numpy_version in NUMPY_VERSIONS:
        for pandas_version in PANDAS_VERSIONS:
            path = 'dockerfiles/{numpy_version}/{pandas_version}'.format(**locals())
            os.makedirs(path, exist_ok=True)

            with open('{path}/Dockerfile'.format(**locals()), 'w') as f:
                f.write('# FILE GENERATED AUTOMATICALLY, DO NOT EDIT MANUALLY\n\n')
                f.write(template.format(**locals()))


if __name__ == '__main__':
    main()
