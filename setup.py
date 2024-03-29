from setuptools import setup, find_packages
# from setuptools_git_versioning import get_version

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='awsservice',

    # generate version for package
    # setuptools_git_versioning={"enabled": True},
    # setup_requires=["setuptools-git-versioning<2"],
    # version=get_version(),
    version='0.0.8',

    description="A small example package for AWS: S3, EC2, CloudWatch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Vitalik Kost',
    author_email='vitalii.kostyreva@gmail.com',
    packages=find_packages(),
    url='https://github.com/Vitalikys/AWS_s3_app',
    install_requires=[
        'boto3',
        'pytz',
        'botocore',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
