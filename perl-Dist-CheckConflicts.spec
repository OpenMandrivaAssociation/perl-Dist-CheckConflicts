%define upstream_name    Dist-CheckConflicts
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Declare version conflicts for your dist
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


