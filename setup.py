import setuptools
from pip.req import parse_requirements


setuptools.setup(
    name="VisionTool",
    version="0.0.1",
    author="Vito Paolo Pastore, Matteo Moro, Francesca Odone",
    author_email="vitopaolopastore@gmail.com",
    description="Toolbox for semantic features extraction ",
    long_description="Toolbox for semantic features extraction ",
    url="https://github.com/Malga-Vision/VisionTool.git",
    packages=setuptools.find_packages(),
    install_requirements = ['pyparsing==2.4.7',
'python-dateutil==2.8.1',
'pytz==2020.1',
'PyWavelets==1.1.1',
'PyYAML==5.3.1',
'requests==2.23.0',
'requests-oauthlib==1.3.0',
'rsa==4.0',
'scikit-image==0.17.2',
'scikit-learn==0.23.1',
'scipy==1.4.1',
'segmentation-models==1.0.1',
'six==1.15.0',
''sklearn==0.0',
'tensorboard==2.2.2',
'tensorboard-plugin-wit==1.6.0.post3',
'tensorflow-estimator==1.13.0',
'tensorflow-gpu==2.2.0',
'tensorflow-gpu-estimator>=2.4.0',
'termcolor==1.1.0',
'threadpoolctl==2.1.0',
'tifffile==2020.6.3',
'tqdm==4.46.1',
'urllib3==1.25.9',
'Werkzeug==1.0.1',
'wincertstore==0.2',
'wrapt==1.12.1',
'wxPython==4.1.0',
'zipp==3.1.0'        ]                    
    
)
