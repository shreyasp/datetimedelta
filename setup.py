from setuptools import setup

setup(
	name='datetimedelta',
	version='0.0.1',
	description='Extends Ruby date time delta functionality to Python',
	author='Shreyas Patil',
	author_email='shreyaspatil87@gmail.com',
	packages=[
		'datetimedelta'
	],
	url='https://github.com/shreyasp/datetimedelta',
	license='MIT',
	install_requires=[
		'python-dateutil'
	],
	keywords=[
		'datetime',
		'delta',
		'inline'
	],
	test_suite='nose.collector',
	tests_require=[
		'nose'
	]
)