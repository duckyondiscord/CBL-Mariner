# remirepo/fedora spec file for php-sebastian-cli-parser
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# namespace
%global php_home     %{_datadir}/php

Name:           php-sebastian-cli-parser
Version:        1.0.1
Release:        5%{?dist}
Summary:        Library for parsing CLI options

License:        BSD
URL:            https://github.com/sebastianbergmann/cli-parser
# git snapshot to retrieve test suite
Source0:        https://github.com/sebastianbergmann/cli-parser/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-pcre
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3"
# temporary ignore min version, test suite passes with 9.2
BuildRequires:  phpunit9 >= 9.2
%endif

# from composer.json, "require": {
#        "php": ">=7.3",
Requires:       php(language) >= 7.3
# from phpcompatinfo report for version 1.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/cli-parser) = %{version}


%description
Library for parsing $_SERVER['argv'], extracted from phpunit/phpunit.

Autoloader: %{php_home}/SebastianBergmann/CliParser/autoload.php


%prep
%setup -q 


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/CliParser


%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/SebastianBergmann/CliParser/autoload.php \
     %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/SebastianBergmann
     %{php_home}/SebastianBergmann/CliParser


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Thu Aug 13 2020 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package
