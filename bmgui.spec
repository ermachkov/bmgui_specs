Name:           bmgui
Version:        0.1
Release:        936%{?dist} 
Summary:        Sibek Balance Machine GUI

Group:          Applications/System
License:        GPLv2+
URL:            http://www.sibek.ru
Source0:        %{name}-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}%{release}-root-%(%{__id_u} -n)

BuildArch:      x86_64

Requires:       xinput_calibrator
Requires:	bmgui-fw = 0.3-7.fc17
Requires:       xinput
Requires:       roxterm
Requires:	php-cli
Requires:       clanlib

%description
Sibek Balance Machine GUI for KonsulM

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/i18n
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/init.d
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

install -pm 755 bmgui $RPM_BUILD_ROOT%{_bindir}/
install -pm 755 files/bmgui_xinput_calibrator $RPM_BUILD_ROOT%{_bindir}/
install -pm 755 bmgui_start $RPM_BUILD_ROOT%{_bindir}/
install -pm 755 files/bmgui_update $RPM_BUILD_ROOT%{_bindir}/
install -pm 755 files/bmgui_update_fw $RPM_BUILD_ROOT%{_bindir}/
install -pm 755 files/bmgui_get_ini $RPM_BUILD_ROOT%{_bindir}/
install -pm 755 files/bmgui_push_file $RPM_BUILD_ROOT%{_bindir}/

install -pm 644 data/files/id_rsa $RPM_BUILD_ROOT%{_datadir}/%{name}/files/
install -pm 644 data/scripts/wizard.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/balance_progress.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/common.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/sound.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/stats.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/start_screen.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/keyboard.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/main_menu.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/main_screen.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/disk_menu.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/layout_menu.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/message.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/scripts/oscilloscope.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/
install -pm 644 data/sprites/main_screen/texture1.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture10.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture8.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture9.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture7.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/sprites.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture2.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture3.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture11.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture4.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture0.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/wheel.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/keyboard.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/start_screen.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture6.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/disk_menu.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture0.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/layout_menu.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/resources.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture5.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture12.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/misc.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/main_screen.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/texture1.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/message.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/scream.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_screen/scream.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_screen/
install -pm 644 data/sprites/main_menu/texture1.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/oscilloscope.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/stats.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture7.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/sprites.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture2.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture3.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture4.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture0.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/main_menu.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture6.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture0.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture8.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture9.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/wizard.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/resources.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture5.png $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/icons.layers $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/sprites/main_menu/texture1.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/sprites/main_menu/
install -pm 644 data/fonts/LiberationSans-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/
install -pm 644 data/fonts/LiberationSans-Regular.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/
install -pm 644 data/fonts/main_menu.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/
install -pm 644 data/fonts/DS-DIGIB.TTF $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/
install -pm 644 data/fonts/main_screen.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/
install -pm 644 data/fonts/wqy-microhei.ttc $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/
install -pm 644 data/sounds/ru/diam_not_entered.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/ofs_not_entered.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/round_off.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/round_on.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/sizes_not_entered.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/width_not_entered.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/ruler.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/stop_key.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/ruler_success.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/balance_success.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/key.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/sounds.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/start_key.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/left_10.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/left_100.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/left_15.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/left_20.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/left_25.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/        
install -pm 644 data/sounds/ru/left_30.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/         
install -pm 644 data/sounds/ru/left_35.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/          
install -pm 644 data/sounds/ru/left_40.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/left_45.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/left_5.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/left_50.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/          
install -pm 644 data/sounds/ru/left_55.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/left_60.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/          
install -pm 644 data/sounds/ru/left_65.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/left_70.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/left_75.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/         
install -pm 644 data/sounds/ru/left_80.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/       
install -pm 644 data/sounds/ru/left_85.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/          
install -pm 644 data/sounds/ru/left_90.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/       
install -pm 644 data/sounds/ru/left_95.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/         
install -pm 644 data/sounds/ru/right_10.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/        
install -pm 644 data/sounds/ru/right_100.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/        
install -pm 644 data/sounds/ru/right_15.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/        
install -pm 644 data/sounds/ru/right_20.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/          
install -pm 644 data/sounds/ru/right_25.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/        
install -pm 644 data/sounds/ru/right_30.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/right_35.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/          
install -pm 644 data/sounds/ru/right_40.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/right_45.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/right_5.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/right_50.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/right_55.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/right_60.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/          
install -pm 644 data/sounds/ru/right_65.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/right_70.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/           
install -pm 644 data/sounds/ru/right_75.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/         
install -pm 644 data/sounds/ru/right_80.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/          
install -pm 644 data/sounds/ru/right_85.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/         
install -pm 644 data/sounds/ru/right_90.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/        
install -pm 644 data/sounds/ru/right_95.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/accel.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/alu_disk_selected.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/decel.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/dynamic_balance.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/emergency_stop.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/measure.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/menu.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/num_spikes_selected.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/options.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/safe_shutdown.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/shutdown.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/static_balance.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/steel_disk_selected.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/truck_disk_selected.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/user_1.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/user_1_selected.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/user_2.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/user_2_selected.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/wheel_is_balanced.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/auto_rotation_left.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/auto_rotation_right.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/auto_rotation_on.wav  $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/auto_rotation_off.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/error.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/push_cover.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/overload.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/balance.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/balance_1_weight.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/balance_2_weight.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/calibration_display.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/calibration_wheel.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/recalc.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/sounds/ru/scream.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/ru/
install -pm 644 data/i18n/en.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/i18n/
install -pm 644 data/i18n/ru.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/i18n/
install -pm 644 data/i18n/cn.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/i18n/
install -pm 644 data/main.lua $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -pm 644 files/bmgui.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -pm 644 files/bmgui.desktop $RPM_BUILD_ROOT%{_datadir}/applications/
install -pm 644 files/bminfo $RPM_BUILD_ROOT%{_sysconfdir}/
install -pm 644 files/bmgui.xml $RPM_BUILD_ROOT%{_sysconfdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_bindir}
%{_bindir}/bmgui
%{_bindir}/bmgui_xinput_calibrator
%{_bindir}/bmgui_start
%{_bindir}/bmgui_update
%{_bindir}/bmgui_update_fw
%{_bindir}/bmgui_get_ini
%{_bindir}/bmgui_push_file

%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/files/id_rsa
%{_datadir}/%{name}/scripts/wizard.lua
%{_datadir}/%{name}/scripts/balance_progress.lua
%{_datadir}/%{name}/scripts/common.lua
%{_datadir}/%{name}/scripts/stats.lua
%{_datadir}/%{name}/scripts/start_screen.lua
%{_datadir}/%{name}/scripts/keyboard.lua
%{_datadir}/%{name}/scripts/main_menu.lua
%{_datadir}/%{name}/scripts/main_screen.lua
%{_datadir}/%{name}/scripts/disk_menu.lua
%{_datadir}/%{name}/scripts/layout_menu.lua
%{_datadir}/%{name}/scripts/message.lua
%{_datadir}/%{name}/scripts/oscilloscope.lua
%{_datadir}/%{name}/scripts/sound.lua
%{_datadir}/%{name}/sprites/main_screen/texture1.png
%{_datadir}/%{name}/sprites/main_screen/texture10.png
%{_datadir}/%{name}/sprites/main_screen/texture8.png
%{_datadir}/%{name}/sprites/main_screen/texture7.png
%{_datadir}/%{name}/sprites/main_screen/sprites.lua
%{_datadir}/%{name}/sprites/main_screen/texture2.png
%{_datadir}/%{name}/sprites/main_screen/texture3.png
%{_datadir}/%{name}/sprites/main_screen/texture9.png
%{_datadir}/%{name}/sprites/main_screen/texture11.png
%{_datadir}/%{name}/sprites/main_screen/texture4.png
%{_datadir}/%{name}/sprites/main_screen/texture0.jpg
%{_datadir}/%{name}/sprites/main_screen/wheel.layers
%{_datadir}/%{name}/sprites/main_screen/keyboard.layers
%{_datadir}/%{name}/sprites/main_screen/start_screen.layers
%{_datadir}/%{name}/sprites/main_screen/texture6.png
%{_datadir}/%{name}/sprites/main_screen/disk_menu.layers
%{_datadir}/%{name}/sprites/main_screen/texture0.png
%{_datadir}/%{name}/sprites/main_screen/layout_menu.layers
%{_datadir}/%{name}/sprites/main_screen/resources.xml
%{_datadir}/%{name}/sprites/main_screen/texture5.png
%{_datadir}/%{name}/sprites/main_screen/texture12.png
%{_datadir}/%{name}/sprites/main_screen/misc.layers
%{_datadir}/%{name}/sprites/main_screen/main_screen.layers
%{_datadir}/%{name}/sprites/main_screen/texture1.jpg
%{_datadir}/%{name}/sprites/main_screen/message.layers
%{_datadir}/%{name}/sprites/main_menu/texture1.png
%{_datadir}/%{name}/sprites/main_menu/oscilloscope.layers
%{_datadir}/%{name}/sprites/main_menu/stats.layers
%{_datadir}/%{name}/sprites/main_menu/texture7.png
%{_datadir}/%{name}/sprites/main_menu/sprites.lua
%{_datadir}/%{name}/sprites/main_menu/texture2.png
%{_datadir}/%{name}/sprites/main_menu/texture3.png
%{_datadir}/%{name}/sprites/main_menu/texture4.png
%{_datadir}/%{name}/sprites/main_menu/texture0.jpg
%{_datadir}/%{name}/sprites/main_menu/texture8.png
%{_datadir}/%{name}/sprites/main_menu/texture9.png
%{_datadir}/%{name}/sprites/main_menu/main_menu.layers
%{_datadir}/%{name}/sprites/main_menu/texture6.png
%{_datadir}/%{name}/sprites/main_menu/texture0.png
%{_datadir}/%{name}/sprites/main_menu/wizard.layers
%{_datadir}/%{name}/sprites/main_menu/resources.xml
%{_datadir}/%{name}/sprites/main_menu/texture5.png
%{_datadir}/%{name}/sprites/main_menu/icons.layers
%{_datadir}/%{name}/sprites/main_menu/texture1.jpg
%{_datadir}/%{name}/sprites/main_screen/scream.jpg
%{_datadir}/%{name}/sprites/main_screen/scream.xml
%{_datadir}/%{name}/fonts/LiberationSans-Bold.ttf
%{_datadir}/%{name}/fonts/LiberationSans-Regular.ttf
%{_datadir}/%{name}/fonts/main_menu.xml
%{_datadir}/%{name}/fonts/DS-DIGIB.TTF
%{_datadir}/%{name}/fonts/main_screen.xml
%{_datadir}/%{name}/fonts/wqy-microhei.ttc
%{_datadir}/%{name}/sounds/ru/diam_not_entered.wav
%{_datadir}/%{name}/sounds/ru/ofs_not_entered.wav
%{_datadir}/%{name}/sounds/ru/round_off.wav
%{_datadir}/%{name}/sounds/ru/round_on.wav
%{_datadir}/%{name}/sounds/ru/sizes_not_entered.wav
%{_datadir}/%{name}/sounds/ru/width_not_entered.wav
%{_datadir}/%{name}/sounds/ru/ruler.wav
%{_datadir}/%{name}/sounds/ru/stop_key.wav
%{_datadir}/%{name}/sounds/ru/ruler_success.wav
%{_datadir}/%{name}/sounds/ru/balance_success.wav
%{_datadir}/%{name}/sounds/ru/key.wav
%{_datadir}/%{name}/sounds/ru/sounds.xml
%{_datadir}/%{name}/sounds/ru/start_key.wav
%{_datadir}/%{name}/sounds/ru/left_10.wav
%{_datadir}/%{name}/sounds/ru/left_100.wav
%{_datadir}/%{name}/sounds/ru/left_15.wav
%{_datadir}/%{name}/sounds/ru/left_20.wav
%{_datadir}/%{name}/sounds/ru/left_25.wav
%{_datadir}/%{name}/sounds/ru/left_30.wav
%{_datadir}/%{name}/sounds/ru/left_35.wav
%{_datadir}/%{name}/sounds/ru/left_40.wav
%{_datadir}/%{name}/sounds/ru/left_45.wav
%{_datadir}/%{name}/sounds/ru/left_5.wav 
%{_datadir}/%{name}/sounds/ru/left_50.wav
%{_datadir}/%{name}/sounds/ru/left_55.wav
%{_datadir}/%{name}/sounds/ru/left_60.wav
%{_datadir}/%{name}/sounds/ru/left_65.wav
%{_datadir}/%{name}/sounds/ru/left_70.wav
%{_datadir}/%{name}/sounds/ru/left_75.wav
%{_datadir}/%{name}/sounds/ru/left_80.wav
%{_datadir}/%{name}/sounds/ru/left_85.wav
%{_datadir}/%{name}/sounds/ru/left_90.wav
%{_datadir}/%{name}/sounds/ru/left_95.wav
%{_datadir}/%{name}/sounds/ru/right_10.wav
%{_datadir}/%{name}/sounds/ru/right_100.wav
%{_datadir}/%{name}/sounds/ru/right_15.wav
%{_datadir}/%{name}/sounds/ru/right_20.wav
%{_datadir}/%{name}/sounds/ru/right_25.wav
%{_datadir}/%{name}/sounds/ru/right_30.wav
%{_datadir}/%{name}/sounds/ru/right_35.wav
%{_datadir}/%{name}/sounds/ru/right_40.wav
%{_datadir}/%{name}/sounds/ru/right_45.wav
%{_datadir}/%{name}/sounds/ru/right_5.wav 
%{_datadir}/%{name}/sounds/ru/right_50.wav
%{_datadir}/%{name}/sounds/ru/right_55.wav
%{_datadir}/%{name}/sounds/ru/right_60.wav
%{_datadir}/%{name}/sounds/ru/right_65.wav
%{_datadir}/%{name}/sounds/ru/right_70.wav
%{_datadir}/%{name}/sounds/ru/right_75.wav
%{_datadir}/%{name}/sounds/ru/right_80.wav
%{_datadir}/%{name}/sounds/ru/right_85.wav
%{_datadir}/%{name}/sounds/ru/right_90.wav
%{_datadir}/%{name}/sounds/ru/right_95.wav
%{_datadir}/%{name}/sounds/ru/accel.wav
%{_datadir}/%{name}/sounds/ru/alu_disk_selected.wav
%{_datadir}/%{name}/sounds/ru/decel.wav
%{_datadir}/%{name}/sounds/ru/dynamic_balance.wav
%{_datadir}/%{name}/sounds/ru/emergency_stop.wav
%{_datadir}/%{name}/sounds/ru/measure.wav
%{_datadir}/%{name}/sounds/ru/menu.wav
%{_datadir}/%{name}/sounds/ru/num_spikes_selected.wav
%{_datadir}/%{name}/sounds/ru/options.wav
%{_datadir}/%{name}/sounds/ru/safe_shutdown.wav
%{_datadir}/%{name}/sounds/ru/shutdown.wav
%{_datadir}/%{name}/sounds/ru/static_balance.wav
%{_datadir}/%{name}/sounds/ru/steel_disk_selected.wav
%{_datadir}/%{name}/sounds/ru/truck_disk_selected.wav
%{_datadir}/%{name}/sounds/ru/user_1.wav
%{_datadir}/%{name}/sounds/ru/user_1_selected.wav
%{_datadir}/%{name}/sounds/ru/user_2.wav
%{_datadir}/%{name}/sounds/ru/user_2_selected.wav
%{_datadir}/%{name}/sounds/ru/wheel_is_balanced.wav
%{_datadir}/%{name}/sounds/ru/auto_rotation_left.wav 
%{_datadir}/%{name}/sounds/ru/auto_rotation_right.wav
%{_datadir}/%{name}/sounds/ru/balance.wav
%{_datadir}/%{name}/sounds/ru/balance_1_weight.wav
%{_datadir}/%{name}/sounds/ru/balance_2_weight.wav
%{_datadir}/%{name}/sounds/ru/calibration_display.wav
%{_datadir}/%{name}/sounds/ru/calibration_wheel.wav
%{_datadir}/%{name}/sounds/ru/auto_rotation_on.wav
%{_datadir}/%{name}/sounds/ru/auto_rotation_off.wav
%{_datadir}/%{name}/sounds/ru/error.wav
%{_datadir}/%{name}/sounds/ru/push_cover.wav
%{_datadir}/%{name}/sounds/ru/overload.wav
%{_datadir}/%{name}/sounds/ru/recalc.wav
%{_datadir}/%{name}/sounds/ru/scream.wav
%{_datadir}/%{name}/i18n/en.lua
%{_datadir}/%{name}/i18n/ru.lua
%{_datadir}/%{name}/i18n/cn.lua
%{_datadir}/%{name}/main.lua

%defattr(-,root,root,-)
%dir %{_datadir}/pixmaps
%{_datadir}/pixmaps/bmgui.png

%defattr(-,root,root,-)
%dir %{_datadir}/applications
%{_datadir}/applications/bmgui.desktop

%defattr(-,root,root,-)
%dir %{_sysconfdir}
%{_sysconfdir}/bminfo
%{_sysconfdir}/bmgui.xml

