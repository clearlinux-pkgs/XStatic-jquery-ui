#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-jquery-ui
Version  : 1.12.0.1
Release  : 18
URL      : https://pypi.python.org/packages/source/X/XStatic-jquery-ui/XStatic-jquery-ui-1.12.0.1.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-jquery-ui/XStatic-jquery-ui-1.12.0.1.tar.gz
Summary  : jquery-ui 1.12.0 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-jquery-ui-python3
Requires: XStatic-jquery-ui-python
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
Requires: XStatic-jquery-ui-python3
Provides: xstatic-jquery-ui-python

%description python
python components for the XStatic-jquery-ui package.


%package python3
Summary: python3 components for the XStatic-jquery-ui package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-jquery-ui package.


%prep
%setup -q -n XStatic-jquery-ui-1.12.0.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534029212
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
