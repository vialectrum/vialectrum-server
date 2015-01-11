from setuptools import setup

setup(
    name="vialectrum-server",
    version="0.9",
    scripts=['run_vialectrum_server','vialectrum-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp',
        'electrumserver.stratum_http'
    ],
    description="Viacoin Vialectrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/vialectrum/vialectrum-server/",
    long_description="""Server for the Vialectrum Lightweight Viacoin Wallet"""
)


