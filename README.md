# Neptune

## Installation

These instructions assume you have already installed git and homebrew for MacOS

This repository uses [proto](https://moonrepo.dev/docs/proto/) to manage dependencies install it with the following:

MacOS

```bash
brew install git unzip gzip xz

curl -fsSL https://moonrepo.dev/install/proto.sh | bash
```

Linux

```bash
apt-get install git unzip gzip xz-utils

curl -fsSL https://moonrepo.dev/install/proto.sh | bash
```

Windows

```bash
irm https://moonrepo.dev/install/proto.ps1 | iex

Set-ExecutionPolicy RemoteSigned
```

Then to clone this repository and install toolchains run:

```bash
git clone https://github.com/CalebNeal07/Neptune.git

proto use
```

> [!NOTE]
> Every project should automatically install its own dependencies on first build, but these are not installed with the above command only the necessary toolchains to run each project are.

## Usage
