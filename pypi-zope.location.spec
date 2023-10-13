#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-zope.location
Version  : 5.0
Release  : 54
URL      : https://files.pythonhosted.org/packages/eb/f9/1fb7a001feb5fec6f180ef3610169f1cbef76e8c015c52409c2d18b7fac4/zope.location-5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/eb/f9/1fb7a001feb5fec6f180ef3610169f1cbef76e8c015c52409c2d18b7fac4/zope.location-5.0.tar.gz
Summary  : Zope Location
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.location-license = %{version}-%{release}
Requires: pypi-zope.location-python = %{version}-%{release}
Requires: pypi-zope.location-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.interface)
BuildRequires : pypi(zope.proxy)
BuildRequires : pypi(zope.schema)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
===================
``zope.location``
===================
.. image:: https://img.shields.io/pypi/v/zope.location.svg
:target: https://pypi.python.org/pypi/zope.location/
:alt: Latest release

%package license
Summary: license components for the pypi-zope.location package.
Group: Default

%description license
license components for the pypi-zope.location package.


%package python
Summary: python components for the pypi-zope.location package.
Group: Default
Requires: pypi-zope.location-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.location package.


%package python3
Summary: python3 components for the pypi-zope.location package.
Group: Default
Requires: python3-core
Provides: pypi(zope.location)
Requires: pypi(setuptools)
Requires: pypi(zope.interface)
Requires: pypi(zope.proxy)
Requires: pypi(zope.schema)

%description python3
python3 components for the pypi-zope.location package.


%prep
%setup -q -n zope.location-5.0
cd %{_builddir}/zope.location-5.0
pushd ..
cp -a zope.location-5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695160819
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.location
cp %{_builddir}/zope.location-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.location/a0b53f43aab58b46bf79ba756c50771c605ab4c5 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.location/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
