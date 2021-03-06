#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-jquery-ui
Version  : 1.12.1.1
Release  : 28
URL      : https://files.pythonhosted.org/packages/e6/5a/883b22dad1d3e01708312d71c5bc63d543d66cef9b448c1cf85379d64fb3/XStatic-jquery-ui-1.12.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e6/5a/883b22dad1d3e01708312d71c5bc63d543d66cef9b448c1cf85379d64fb3/XStatic-jquery-ui-1.12.1.1.tar.gz
Summary  : jquery-ui 1.12.1 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-jquery-ui-python = %{version}-%{release}
Requires: XStatic-jquery-ui-python3 = %{version}-%{release}
Requires: XStatic-jQuery
BuildRequires : XStatic
BuildRequires : XStatic-jQuery
BuildRequires : buildreq-distutils3
Patch1: build.patch

%description
-----------------
        
        jquery-ui javascript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-jquery-ui package.
Group: Default
Requires: XStatic-jquery-ui-python3 = %{version}-%{release}
Provides: xstatic-jquery-ui-python

%description python
python components for the XStatic-jquery-ui package.


%package python3
Summary: python3 components for the XStatic-jquery-ui package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_jquery_ui)
Requires: pypi(xstatic_jquery)

%description python3
python3 components for the XStatic-jquery-ui package.


%prep
%setup -q -n XStatic-jquery-ui-1.12.1.1
cd %{_builddir}/XStatic-jquery-ui-1.12.1.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583695625
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
