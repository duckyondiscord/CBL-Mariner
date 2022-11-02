# remirepo/fedora spec file for php-sebastian-version3
#
# Copyright (c) 2013-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Namespace (fake ns_project as not PSR-4 compliant)
%global php_home     %{_datadir}/php

Name:           php-sebastian-version3
Version:        3.0.2
Release:        5%{?dist}
Summary:        Managing the version number of Git-hosted PHP projects, version 3

License:        BSD
URL:            https://github.com/sebastianbergmann/version
Source0:        https://github.com/sebastianbergmann/version/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
Requires:       git
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/version) = %{version}


%description
Library that helps with managing the version number
of Git-hosted PHP projects.


%prep
%setup -q 


%build
: Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
# Not PSR-4 compliant, but ok as we use a classmap
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/Version3


%check
: check autoloader
php -r '
require "%{buildroot}%{php_home}/SebastianBergmann/Version3/autoload.php";
exit (class_exists("SebastianBergmann\\Version") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/SebastianBergmann
     %{php_home}/SebastianBergmann/Version3


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1 (no change)
- sources from git snapshot

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 7.3
- rename to php-sebastian-version3
- move to /usr/share/php/SebastianBergmann/Version3

* Sat Nov 26 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1 (no change)
- switch to fedora/autoloader

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- raise minimal php version to 5.6

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6
- generate autoloader
- fix PSR-0 layout

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Sun Jan  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- fix scriptlet
- drop pear compatibility provides
- fix license usage

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 1.0.3-3
- composer dependencies

* Sat Mar  8 2014 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- move from pear channel to github sources because of
  https://github.com/sebastianbergmann/phpunit/wiki/Release-Announcement-for-PHPUnit-4.0.0
- add %%check
- add missing dependency on git

* Thu Feb 13 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Thu May 30 2013 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Apr  4 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
