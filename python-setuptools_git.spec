#
# Conditional build:
%bcond_with	tests	# unit tests (need git configured)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Setuptools revision control system plugin for Git
Summary(pl.UTF-8):	Wtyczka setuptools do systemu kontroli wersji Git
Name:		python-setuptools_git
Version:	1.2
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools-git/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools-git/setuptools-git-%{version}.tar.gz
# Source0-md5:	40b2ef7687a384ea144503c2e5bc67e2
URL:		https://github.com/msabramo/setuptools-git
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
%if %{with tests}
BuildRequires:	git-core
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a plugin for setuptools that enables git integration. Once
installed, Setuptools can be told to include in a package distribution
all the files tracked by git. This is an alternative to explicit
inclusion specifications with MANIFEST.in.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczkę do setuptools włączającą integrację z
gitem. Po zainstalowaniu jej, setuptools można przekazać, żeby
dołączyć do dystrybucji pakietu wszystkie pliki śledzone przez gita -
jest to alternatywa dla jawnego określenia plików w MANIFEST.in.

%package -n python3-setuptools_git
Summary:	Setuptools revision control system plugin for Git
Summary(pl.UTF-8):	Wtyczka setuptools do systemu kontroli wersji Git
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-setuptools_git
This is a plugin for setuptools that enables git integration. Once
installed, Setuptools can be told to include in a package distribution
all the files tracked by git. This is an alternative to explicit
inclusion specifications with MANIFEST.in.

%description -n python3-setuptools_git -l pl.UTF-8
Ten pakiet zawiera wtyczkę do setuptools włączającą integrację z
gitem. Po zainstalowaniu jej, setuptools można przekazać, żeby
dołączyć do dystrybucji pakietu wszystkie pliki śledzone przez gita -
jest to alternatywa dla jawnego określenia plików w MANIFEST.in.

%prep
%setup -q -n setuptools-git-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.txt LICENSE.txt README.rst TODO.txt
%{py_sitescriptdir}/setuptools_git
%{py_sitescriptdir}/setuptools_git-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-setuptools_git
%defattr(644,root,root,755)
%doc AUTHORS.txt LICENSE.txt README.rst TODO.txt
%{py3_sitescriptdir}/setuptools_git
%{py3_sitescriptdir}/setuptools_git-%{version}-py*.egg-info
%endif
