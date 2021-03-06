from setuptools import setup, find_packages
import os

with open(os.path.join(
        os.path.dirname(__file__),
        'sixfeetup', 'workflow', 'featured', 'version.txt')) as version_txt:
    version = version_txt.read().strip()

setup(name='sixfeetup.workflow.featured',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='lucie',
      author_email='lucie@sixfeetup.com',
      url='http://svn.plone.org/svn/plone/plone.example',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sixfeetup', 'sixfeetup.workflow'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'sixfeetup.catalogoverrides',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """
      )
