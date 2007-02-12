#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GraphViz
%define		pnam	Makefile
Summary:	Create Makefile graphs using GraphViz
Summary(pl.UTF-8):   Tworzenie grafów z plików Makefile wykorzystując GraphViz
Name:		perl-GraphViz-Makefile
Version:	1.15
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	432f7437c71ff72f815e32b8de5f9af3
URL:		http://search.cpan.org/~srezic/GraphViz-Makefile-1.12/
BuildRequires:	perl-GraphViz
BuildRequires:	perl-Make
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
