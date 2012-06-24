
%define		module	Pyrex

Summary:	Language for writing Python Extension Modules
Summary(pl):	J�zyk s�u��cy do pisania modu��w rozszerzaj�cych Pythona
Name:		python-%{module}
Version:	0.9.3
Release:	6
License:	free
Group:		Libraries/Python
Source0:	http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/%{module}-%{version}.tar.gz
# Source0-md5:	63c4cb884d6b777d3806f9669ba5feba
Patch0:         %{name}-py24-swig_sources.patch
Patch1:		%{name}-gcc4.patch
URL:		http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
BuildRequires:	python
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.c

%description
Pyrex lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python.

%description -l pl
Pyrex pozwala pisa� kod zawieraj�cy dane Pythona i j�zyka C po��czone
w jakikolwiek spos�b i kompiluje to jako rozszerzenie C dla Pythona.

%package examples
Summary:	Examples for Pyrex language
Summary(pl):	Przyk�ady program�w w j�zyku Pyrex
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Pyrex language.

%description examples -l pl
Pakiet zawieraj�cy przyk�adowe programy napisane w j�zyku Pyrex.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py_sitedir} \
	-O2

find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" -a ! -name 'Lexicon.py' -exec rm -f {} \;

cp -ar Demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
