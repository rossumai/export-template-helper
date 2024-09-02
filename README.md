# MEGA helper
This command line tool is used to process Jinja2 templates using Rossum annotation payload and to generate settings of the MEGA extension.
MEGA is an internal name for Custom Format Payload extension.

# Installation guide
```
brew install pipx
pipx ensurepath
pipx install .
```

# User guide
There are two use cases this tool helps you with, they are listed below. They render output to stdout.

## Process Jinja2 template
Locally process Jinja2 template using annotation payload either from local file or Rossum API. See the sample commands below.

Process template using locally stored payload:
```
poetry run mega-helper -p -t {template file path} -l {payload file path}
poetry run mega-helper -p -t template.json -l data.json
```

Process template using data from Rossum API:
```
poetry run mega-helper -p -t {template file path} -a {annotationId} -o {hookId} -u {baseUrl} -n {authToken}
poetry run mega-helper -p -t template.json -a 123456 -o 123456 -u https://your-org.rossum.app/api/v1 -n 4ccf1d11a42070e70c132f2678076b412489339f 
```

In case of a local file, the full annotation payload as Rossum generates it is expected.

## Generate MEGA settings
Generate configuration of the Custom Payload Format extension using the Jinja2 template and reference key:

```
poetry run mega-helper -g -t template.json -k json
```

## Typical usage (tell it to me like I'm a 6yo)
* Clone this repo `git clone https://github.com/rossumai/mega-helper`
* Install it `pipx install .`
* Add your template to the root
* Note `annotation ID`, `hook ID`, `base URL` and `auth token` and use run this: `poetry run mega-helper -p -t {template file path} -a {annotationId} -o {hookId} -u {baseUrl} -n {authToken}`
* Keep editing the template until it's ready
* When the template is ready, run this: `poetry run mega-helper -g -t {template file path} -k {export reference key}`
* Copy the configuration from stdout to MEGA extension config

# Full list of parameters
|param|description|
|--|--|
|`-p --process`|process a local Jinja2 template with Rossum annotation payload|
|`-g --generate`|generate MEGA extension configuration using a local Jinja2 template|
|`-t --templatePath`|path to local Jinja2 template|
|`-l --payloadPath`|path to local file with Rossum annotation payload|
|`-a --annotationId`|annotation ID to fetch payload from Rossum API|
|`-n --token`|Rossum API token|
|`-o --hookId`|Rossum hook ID|
|`-u --url`|Rossum base API URL|
|`-k --key`|Export reference key|
