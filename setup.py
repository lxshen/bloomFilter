# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:   # 这里就是读取readme文件的内容了。
    long_description = fh.read()


setup(
    name='lx_bloomfilter',  # '库的名称,一般写成文件夹的名字就可以了，也有的人不写成文件夹的名字，那么pip install和具体的import使用时候就不一样了，用起来会十分蛋疼，有一些包就是这样的。比如一个包，安装时候是pip install  xxx,但当你要使用时候要import yyy


    version="0.1.2",                  # 版本，每次发版本都不能重复，每次发版必须改这个地方
    description=(
        'Python implementation Bloom filter'   # 一个简介，别人搜索包时候，这个概要信息会显示在在搜索列表中

    ),
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='lxshen',       # 作者
    author_email='guanghui2017@outlook.com',
    maintainer='lxshen',     # 主要的工作人员
    maintainer_email='guanghui2017@outlook.com',
    license='BSD License',
    # packages=['douban'], # 发布的包名
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/lxshen/bloomFilter.git',   # 这个是连接，一般写github就可以了，会从pypi跳转到这里去
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[              # 这里是依赖列表，表示运行这个包的运行某些功能还需要你安装其他的包
        'redis',
    ]
)