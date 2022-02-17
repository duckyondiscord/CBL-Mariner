Name:           perl-Object-HashBase
Version:        0.009
Release:        3%{?dist}
Summary:        Build hash-based classes
License:        GPL+ or Artistic
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://metacpan.org/release/Object-HashBase
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Object-HashBase-%{version}.tar.gz#/perl-Object-HashBase-%{version}.tar.gz
# Correct shebangs
Patch0:         Object-HashBase-0.008-Normalize-shebang.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Temp)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Remove under-specified dependenices
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(Object::HashBase::Test::HBase.*

%description
This package is used to generate classes based on hash references. Using this
class will give you a new() method, as well as generating accessors you
request.  Generated accessors will be getters, set_ACCESSOR setters will also
be generated for you. You also get constants for each accessor (all caps)
which return the key into the hash for that accessor. Single inheritance is
also supported.

%package tools
Summary:        Generate inlined Object::HashBase Perl module
Requires:       %{name} = %{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Test::More) >= 0.98

%description tools
hashbase_inc.pl script generates a Perl module that contains
a Object::HashBase module mangled into a name space of your choice. It can
also generate the tests for it.

%prep
%setup -q -n Object-HashBase-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Object/HashBase
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Object::HashBase::*

%files tools
%{_bindir}/hashbase_inc.pl
%{perl_vendorlib}/Object/HashBase
%{_mandir}/man3/Object::HashBase::*

%changelog
* Fri Oct 15 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 0.009-3
- Initial CBL-Mariner import from Fedora 32 (license: MIT).

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Petr Pisar <ppisar@redhat.com> - 0.009-1
- 0.009 bump

* Tue Nov 19 2019 Petr Pisar <ppisar@redhat.com> 0.008-1
- Specfile autogenerated by cpanspec 1.78.