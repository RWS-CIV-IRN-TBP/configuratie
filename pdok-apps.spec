#!/usr/bin/rpmbuild -ba

%define         version 1.0.7

Name:           pdok-apps
Version:        %{version}
Release:        1

%define         install_user     apache
%define         prefix          /apps
%define         apps_prefix %{prefix}/geoservices

Summary:        PDOK applications
License:        GPLv3
Group:          Applications/Internet
Packager:       Milo van der Linden

BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-root
Prefix:         %{prefix}

Requires:       httpd
Autoreq:        1

%description
pdokkaart javascript module and applications created for Rijkswaterstaat that use the pdokkaart or the pdokkaart-api. Applications can be found in subpackages.

%package -n pdok-apps-vegetatielegger
Summary:        vegetatielegger
Group:          Applications/Internet
Requires:       pdok-apps
%description -n pdok-apps-vegetatielegger
pdokkaart vegetatielegger application.

%package -n pdok-apps-apps
Summary:        apps
Group:          Applications/Internet
Requires:       pdok-apps
%description -n pdok-apps-apps
pdokkaart based applications.

%prep

%build
rm -Rf vegetatielegger %{buildroot}
rm -Rf pdokkaart %{buildroot}
rm -Rf configuratie %{buildroot}
rm -Rf pdokapps %{buildroot}
svn export -q https://github.com/RWS-CIV-IRN-TBP/vegetatielegger/trunk vegetatielegger
svn export -q https://github.com/RWS-CIV-IRN-TBP/pdokkaart-configuratie/trunk configuratie
svn export -q https://github.com/RWS-CIV-IRN-TBP/pdokkaart-applicaties/trunk pdokapps
svn export -q https://github.com/Geonovum/pdokkaart/trunk pdokkaart

# skip brp-strip* at end of install (not needed for noarch)
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
# services
%{__mkdir} -p $RPM_BUILD_ROOT/%{apps_prefix}
%{__mkdir} -p $RPM_BUILD_ROOT/%{apps_prefix}/apps/pdokkaart/
%{__mkdir} -p $RPM_BUILD_ROOT/%{apps_prefix}/apps/vegetatielegger/
%{__mkdir} -p $RPM_BUILD_ROOT/%{apps_prefix}/apps/pdokapps/
%{__mkdir} -p $RPM_BUILD_ROOT/%{apps_prefix}/httpd.d/

%{__cp} -a pdokkaart/* $RPM_BUILD_ROOT/%{apps_prefix}/apps/pdokkaart/
%{__cp} -a vegetatielegger/* $RPM_BUILD_ROOT/%{apps_prefix}/apps/vegetatielegger/
%{__cp} -a configuratie/pdok_apps.conf $RPM_BUILD_ROOT/%{apps_prefix}/httpd.d/
%{__cp} -a pdokapps/* $RPM_BUILD_ROOT/%{apps_prefix}/apps/pdokapps/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%pre
#nothing
%post -n pdok-apps
/sbin/service httpd reload
%post -n pdok-apps-vegetatielegger

%preun

%postun

%files -n pdok-apps
%defattr(-,%{install_user},%{install_user})
%dir               %{apps_prefix}/apps/pdokkaart
%{apps_prefix}/apps/pdokkaart/*
%dir               %{apps_prefix}/httpd.d
%{apps_prefix}/httpd.d/pdok_apps.conf


%files -n pdok-apps-vegetatielegger
%defattr(-,%{install_user},%{install_user})
%dir               %{apps_prefix}/apps/vegetatielegger
%{apps_prefix}/apps/vegetatielegger/*

%files -n pdok-apps-apps
%defattr(-,%{install_user},%{install_user})
%dir               %{apps_prefix}/apps/pdokapps
%{apps_prefix}/apps/pdokapps/*

%changelog
* Tue Apr  7 2015 Milo van der Linden  1.0.7-1
- Added the pdokkaart-applications
* Tue Apr  7 2015 Milo van der Linden  1.0.6-1
- Building from subversion
* Thu Mar 12 2015 Milo van der Linden  1.0.5-1
- Switched to RWS-CIV-IRN-TBP repository
- Kustlijnkaart added
* Wed Mar 11 2015 Richard Duivenvoorde 1.0.4-1
- Switched to geonovum repository
- Various cosmetic fixes
* Mon Jan 13 2015 Raymond Nijssen      1.0.3-4
- Proxy fix
* Mon Jan 13 2015 Raymond Nijssen      1.0.3-3
- Fix for broken OpenLayers in responsive web pages
* Wed Jan  7 2015 Raymond Nijssen      1.0.3-2
* Tue Jan  6 2015 Raymond Nijssen      1.0.3-1
* Mon Jan  5 2015 Richard Duivenvoorde 1.0.2-1
- Fix for vegetatielegger
* Mon Jan  5 2015 Raymond Nijssen      1.0.1-1
- Fix for IE8
* Wed Nov  5 2014 Milo van der Linden  1.0.0-1
- Initial version.
