Summary:	Neofetch is a CLI system information tool written in BASH
Name:		neofetch
Version:	7.1.0.1
Release:	2
License:	MIT
Group:		Shells
Url:		https://github.com/dylanaraps/neofetch
#Source0:	https://github.com/dylanaraps/neofetch/archive/%{version}/%{name}-%{version}.tar.gz
Source:%{name}-%version.tar.gz
Patch0:		neofetch-fix-layout.patch
BuildArch: 	noarch

%description
Neofetch is a CLI system information tool written in BASH. 
Neofetch displays information about your system next to an 
image, your OS logo, or any ascii file of your choice. 

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

%files
%doc README.md LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
