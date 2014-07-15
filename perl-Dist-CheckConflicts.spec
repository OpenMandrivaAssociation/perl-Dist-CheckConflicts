%define modname	Dist-CheckConflicts
%define modver 0.11

Summary:	Declare version conflicts for your dist

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(List::MoreUtils)
BuildRequires: perl(Module::Runtime)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*



