%define debug_package %{nil}

Name:		clash-for-windows-bin
Version:	0.20.9
Release:        1%{?dist}
Summary:	A Windows/macOS GUI based on Clash 
License: 	GPL

URL:		https://github.com/Fndroid/clash_for_windows_pkg
Source0: https://github.com/Fndroid/clash_for_windows_pkg/releases/download/%{version}/Clash.for.Windows-%{version}-x64-linux.tar.gz
Source1: clash-for-windows.desktop
SOurce2: clash.png
Source3: cfw

BuildArch: x86_64
BuildRequires: tar

%description
Clash for Windows

%prep
%setup -T -b 0 -n "Clash for Windows-%{version}-x64-linux"
cp %{S:1} %{_builddir}
cp %{S:2} %{_builddir}
cp %{S:3} %{_builddir}
sed -i "s/pkgver/%{version}/" %{_builddir}/clash-for-windows.desktop

%install
export DONT_STRIP=1
find . -type f -not \( -name "cfw" -or -name "clash-linux" -or -name "clash-core-service" -or -name "chrome-sandbox" -or -name "*.sh" \) \
        -exec install -Dm 644 {} "%{buildroot}/opt/clash-for-windows-bin"/{} \;
    echo "packaging executable files as 755"
    find . -type f \( -name "cfw" -or -name "clash-linux" -or -name "clash-core-service" -or -name "chrome-sandbox" -or -name "*.sh" \) \
       -exec install -Dm 755 {} "%{buildroot}/opt/clash-for-windows-bin"/{} \;
    install -Dm 755 ../cfw %{buildroot}/usr/bin/cfw 
    install -Dm 644 ../clash.png %{buildroot}/usr/share/pixmaps/clash.png
    install -Dm 644 ../clash-for-windows.desktop %{buildroot}/usr/share/applications/clash-for-windows.desktop

%files
/opt/clash-for-windows-bin/*
%{_bindir}/*
/usr/share/applications/clash-for-windows.desktop
/usr/share/pixmaps/clash.png

%changelog
* Fri Nov 25 2022 indusy
<teririkawaii@outlook.com> - 0.20.9-1
- new version