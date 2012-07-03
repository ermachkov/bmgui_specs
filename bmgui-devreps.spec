Name:           bmgui-devreps
Version:        0.1
Release:        0%{?dist} 
Summary:        Sibek Balance Machine Development Metapackage

Group:          Applications/System
License:        GPLv2+
URL:            http://www.sibek.ru
Source0:        %{name}-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}%{release}-root-%(%{__id_u} -n)

BuildArch:      x86_64

Requires:	xorg-x11-proto-devel
Requires:	gcc
Requires:	autoconf
Requires:	libtool
Requires:	automake
Requires:	libXi-devel
Requires:	gcc-c++
Requires:	zlib-devel
Requires:	mesa-libGL-devel
Requires:	libmikmod-devel
Requires:	libvorbis-devel
Requires:	sqlite-devel
Requires:	pcre-devel
Requires:	libpng-devel
Requires:	libjpeg-turbo-devel
Requires:	freetype-devel
Requires:	fontconfig-devel
Requires:	lua
Requires:	tolua++-devel
Requires:       tolua++
Requires:       alsa-lib-devel


%description
For leasy SATAN Creature

%prep

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
