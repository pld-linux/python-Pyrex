%define		module	Pyrex
Summary:	Language for writing Python Extension Modules
Summary(pl.UTF-8):	Język służący do pisania modułów rozszerzających Pythona
Name:		python-%{module}
Version:	0.9.9
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
Source0:	http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/%{module}-%{version}.tar.gz
# Source0-md5:	515dee67d15d4393841e2d60e8341947
URL:		http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
%pyrequires_eq	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.c

%description
Pyrex lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python.

%description -l pl.UTF-8
Pyrex pozwala pisać kod zawierający dane Pythona i języka C połączone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.

%package examples
Summary:	Examples for Pyrex language
Summary(pl.UTF-8):	Przykłady programów w języku Pyrex
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Pyrex language.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe programy napisane w języku Pyrex.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_install \
	--install-purelib=%{py_sitescriptdir}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" -a ! -name 'Lexicon.py' -exec rm -f {} \;

cp -a Demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/pyrexc
%{py_sitescriptdir}/Pyrex
%{py_sitescriptdir}/Pyrex-*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
