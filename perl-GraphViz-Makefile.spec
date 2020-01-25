#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	GraphViz
%define		pnam	Makefile
Summary:	Create Makefile graphs using GraphViz
Summary(pl.UTF-8):	Tworzenie grafów z plików Makefile wykorzystując GraphViz
Name:		perl-GraphViz-Makefile
Version:	1.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b80f835000ad3adee6d82ab38a2feb4e
URL:		http://search.cpan.org/dist/GraphViz-Makefile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Make)
BuildRequires:	perl-GraphViz
%endif
Requires:	perl-Tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Create Makefile graphs using GraphViz.

%description -l pl.UTF-8
Tworzenie grafów z plików Makefile wykorzystując GraphViz.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/tkgvizmakefile
%{perl_vendorlib}/GraphViz/Makefile.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
