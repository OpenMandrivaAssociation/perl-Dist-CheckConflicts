%define upstream_name    Dist-CheckConflicts
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Declare version conflicts for your dist
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
One shortcoming of the CPAN clients that currently exist is that they have
no way of specifying conflicting downstream dependencies of modules. This
module attempts to work around this issue by allowing you to specify
conflicting versions of modules separately, and deal with them after the
module is done installing.

For instance, say you have a module 'Foo', and some other module 'Bar' uses
'Foo'. If 'Foo' were to change its API in a non-backwards-compatible way,
this would cause 'Bar' to break until it is updated to use the new API.
'Foo' can't just depend on the fixed version of 'Bar', because this will
cause a circular dependency (because 'Bar' is already depending on 'Foo'),
and this doesn't express intent properly anyway - 'Foo' doesn't use 'Bar'
at all. The ideal solution would be for there to be a way to specify
conflicting versions of modules in a way that would let CPAN clients update
conflicting modules automatically after an existing module is upgraded, but
until that happens, this module will allow users to do this manually.

This module accepts a hash of options passed to its 'use' statement, with
these keys being valid:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-4mdv2012.0
+ Revision: 765191
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-3
+ Revision: 763707
- rebuilt for perl-5.14.x

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2
+ Revision: 654314
- rebuild for updated spec-helper

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 629544
- import perl-Dist-CheckConflicts

