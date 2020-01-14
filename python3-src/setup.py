import setuptools

setuptools.setup(
    name="noser-wf-dmx-demo",
    version="0.1",
    scripts=[
        "bin/hello",
        "bin/set-color",
        "bin/color-sequence"
    ],
    install_requires=[
        "pyserial",
    ]
)
