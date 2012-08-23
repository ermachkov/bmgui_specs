Name:           bmgui-fw
%define pversion 6
Version:        0.3
Release:        %{pversion}%{?dist} 
Summary:        Sibek Balance Machine Firmware

Group:          Applications/System
License:        GPLv2+
URL:            http://www.sibek.ru
Source0:        %{name}-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}%{pversion}-root-%(%{__id_u} -n)

BuildArch:      x86_64

%description
Sibek Balance Machine GUI Firmware for KonsulM

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/bmgui
mkdir -p $RPM_BUILD_ROOT%{_datadir}/bmgui/fw

install -pm 755 bmgui_flash $RPM_BUILD_ROOT%{_bindir}/
install -pm 644 bsfw-%{version}-%{pversion}.tbz $RPM_BUILD_ROOT%{_datadir}/bmgui/fw/

%clean
rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
%dir %{_bindir}
%{_bindir}/bmgui_flash

%defattr(-,root,root,-)
%dir %{_datadir}/bmgui
%{_datadir}/bmgui/fw/bsfw-%{version}-%{pversion}.tbz

%pre
SERVER_IP=`expr "\`cat /home/bm/.bmgui/bmgui.xml 2> /dev/null\`" : '.*server_addr" value="\([0-9]*.[0-9]*.[0-9]*.[0-9]*\)'`

if [ "$SERVER_IP" != "" ]; then
  if [ `ping $SERVER_IP -c 1 -W 1 | grep -c req=1` -eq 0 ]; then
  echo ""
  echo "Check network connection to Balance Machine Hardware"
  exit 0
  fi
fi

%post
SERVER_IP=`expr "\`cat /home/bm/.bmgui/bmgui.xml 2> /dev/null\`" : '.*server_addr" value="\([0-9]*.[0-9]*.[0-9]*.[0-9]*\)'`
if [ "$SERVER_IP" != "" ]; then
  bmgui_flash $SERVER_IP %{_datadir}/bmgui/fw/bsfw-%{version}-%{pversion}.tbz
fi
