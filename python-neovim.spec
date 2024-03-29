%global desc Implements support for python plugins in Nvim. Also works as a library for\
connecting to and scripting Nvim processes through its msgpack-rpc API.

%bcond_with sphinx

Name:           python-neovim
Version:	0.4.3
Release:	2

License:        ASL 2.0
Summary:        Python client to Neovim
URL:            https://github.com/neovim/python-client
Source0:        https://github.com/neovim/python-client/archive/%{version}/python-client-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if %{with sphinx}
BuildRequires:  python-sphinx
%endif

%description
%{desc}

%if %{with sphinx}
%package doc
Summary:        Documentation for %{name}

%description doc
%{desc}

This package contains documentation in HTML format.
%endif

%prep
%autosetup -n pynvim-%{version}

%build
%py3_build

%if %{with sphinx}
pushd docs
make html
rm -f _build/html/.buildinfo
popd
%endif

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%if %{with sphinx}
%files doc
%license LICENSE
%doc docs/_build/html
%endif
