#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-RSS
Summary:	POE::Component::RSS - event-based RSS parsing
Summary(pl.UTF-8):	POE::Component::RSS - oparta na zdarzeniach analiza RSS
Name:		perl-POE-Component-RSS
Version:	0.08
Release:	1
License:	BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d11b15431c41e807fde23b3cd0f7e10c
URL:		http://search.cpan.org/dist/POE-Component-RSS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-POE
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-XML-RSS
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module POE::Component::RSS is an event based RSS parsing module.
It wraps XML::RSS and provides a POE based framework for accessing the
information provided.

%description -l pl.UTF-8
Moduł Perla POE::Component::RSS analizuje RSS w oparciu o zdarzenia.
Obudowuje XML::RSS i udostępnia oparty na POE szkielet pozwalający na
dostęp do dostarczanych informacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{perl_vendorlib}/POE/Component/RSS.pm
%{_mandir}/man3/*
