Name:          python-libarchive-c
Version:       2.5
Release:       2%{?dist}
Summary:       Python interface to libarchive
License:       CC0
URL:           https://github.com/Changaco/python-libarchive-c
#Source0:       https://github.com/Changaco/python-libarchive-c/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Source0: https://repo.citrite.net:443/ctx-local-contrib/xs-opam/python-libarchive-c-2.5.tar.gz



BuildRequires: libarchive-devel
BuildRequires: python-setuptools
BuildRequires: python-devel
BuildRequires: pytest
BuildRequires: glibc-common
Requires:      libarchive
BuildArch:     noarch

%description
The libarchive library provides a flexible interface for reading and writing
archives in various formats such as tar and cpio. libarchive also supports
reading and writing archives compressed using various compression filters such
as gzip and bzip2.

A Python interface to libarchive. It uses the standard ctypes module to
dynamically load and access the C library.

%prep
%autosetup -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O2 --skip-build --root %{buildroot}

# Disabled - simplejson bug causes test case failure
#%check
#LC_ALL=en_US.utf8 py.test-%{python_version} -s -vv tests

%files
%doc README.rst
%{python_sitelib}/libarchive*

%changelog
* Mon Feb 27 2017 Christian Lindig <christian.lindig@citrix.com> - 2.5-2
- Download from internal mirror

* Mon Aug 15 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5-1
- Update to latest version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 04 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 2.3-1
- Update to latest release

* Wed May 04 2016 Pavel Raiskup <praiskup@redhat.com> - 2.2-5
- fix the build against new libarchive
- stop requiring libarchive 3.1.2 explicitly

* Wed May 04 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2-4
- Rebuild for libarchive 3.2.0

* Wed Mar  9 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 2.2-3
- Add license text

* Tue Mar  8 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2-2
- Remove debuginfo removal and enable tests

* Sat Dec 05 2015 Dhiru Kholia <dhiru@openwall.com> - 2.2-1
- Initial version
