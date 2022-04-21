%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pycairo

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.21.0
Release:        1%{?dist}
Summary:        Python interface for cairo

License:        LGPL-2.1-only OR MPL-1.1
URL:            https://pycairo.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license COPYING-LGPL-2.1 COPYING-MPL-1.1
%doc README.rst
%{python3_sitearch}/cairo
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Apr 19 2022 Yanis Guenane 1.21.0-1
- Update to 1.21.0

* Wed Nov 24 2021 Evgeni Golov - 1.20.1-2
- Split devel files into own package

* Mon Sep 13 2021 Evgeni Golov - 1.20.1-1
- Initial package.
