#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kblocks
Summary:	Kblocks
Name:		ka5-%{kaname}
Version:	22.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d4ca2a76d018b6da410f885790c221de
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
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
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

%description -l pl.UTF-8
KBlocks jest klasyczną grą w spadające bloki. Ideą gry jest
układać spadające bloki tak, aby tworzyły poziome linie bez przerw.
Kompletne linie są usuwane i robi się więcej miejsca w obszarze gry.
Gdy nie ma już miejsca na spadające bloki, gra się kończy.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
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
%{_datadir}/metainfo/org.kde.kblocks.appdata.xml
%{_datadir}/qlogging-categories5/kblocks.categories
%{_datadir}/knsrcfiles/kblocks.knsrc
