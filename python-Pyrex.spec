Summary:	Language for Writing Python Extension Modules
Summary(pl):	Jêzyk s³u¿±cy do pisania Modu³ów Rozszerzaj±cych Pythona
Name:		python-Pyrex
Version:	0.9.2.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/Pyrex-%{version}.tar.gz
# Source0-md5:	633780217881ae7af8bd45c383fd6990
URL:		http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautocompressdoc	*.c

%description
Pyrex lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python.

%description -l pl
Pyrex pozwala pisaæ kod zawieraj±cy dane Pythona i jêzyka C po³±czone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.

%prep
%setup -q -n Pyrex-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py_sitedir} \
	-O2

find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" -a ! -name 'Lexicon.py' -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*
