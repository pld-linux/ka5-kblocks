%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kblocks
Summary:	Kblocks
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	423b180ca0de447bdedc9ec9e2eefb49
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBlocks is the classic falling blocks game. The idea is to stack the
falling blocks to create horizontal lines without any gaps. When a
line is completed it is removed, and more space is available in the
play area. When there is not enough space for blocks to fall, the game
is over.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kblocks.categories
/etc/xdg/kblocks.knsrc
%attr(755,root,root) %{_bindir}/kblocks
%{_desktopdir}/org.kde.kblocks.desktop
%{_datadir}/config.kcfg/kblocks.kcfg
%{_iconsdir}/hicolor/128x128/apps/kblocks.png
%{_iconsdir}/hicolor/16x16/apps/kblocks.png
%{_iconsdir}/hicolor/22x22/apps/kblocks.png
%{_iconsdir}/hicolor/32x32/apps/kblocks.png
%{_iconsdir}/hicolor/48x48/apps/kblocks.png
%{_iconsdir}/hicolor/64x64/apps/kblocks.png
%{_datadir}/kblocks
%{_datadir}/kxmlgui5/kblocks
%{_datadir}/metainfo/org.kde.kblocks.appdata.xml
