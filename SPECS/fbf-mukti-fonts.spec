# SPDX-License-Identifqier: MIT
%global commit 6f68286463c2c4ef6959080855d6a3bdb26393aa
%global gittag refs/tags/v3.0.2

%global shortcommit %(c=%{commit}; echo ${c:0:7})
Version:   3.0.2
Release:   1%{dist}

URL: http://github.com/mitradranirban/fonts-mukti

%global foundry fbf 
%global fontfamily    mukti         
%global fontlicense       GPlv3+ with exceptions
%global fontlicenses      LICENCE
%global fontdocs          changelog copyright juktakkhor README.md 
%global fontdocsex        %{fontlicenses}
%global fontsummary       Bangla open source Opentype font
%global fonts            *.otf
%global fontconfs        66-0-%{fontpkgname}.conf
BuildRequires: fontforge 
BuildRequires:  fontpackages-devel
Requires:	fontpackages-filesystem

%global fontdescription  %{expand:
This is a one of the earliest Open Source OpenType Bengali / Bangla font It was made by using good quality glyphs of GPLed font bng2-n from Cyberscape Multimedia 
<https://web.archive.org/web/20021113130716/http://www.akruti.com/freedom/>. It was made for Mukta Bangla Font project.
}

Source0: https://github.com/mitradranirban/fonts-mukti/archive/%{commit}.tar.gz
Source1: https://github.com/mitradranirban/fbf-mukti-fonts/raw/main/SOURCES/66-0-fbf-mukti-fonts.conf

%fontpkg 

%prep
%autosetup -n fonts-mukti-%{commit}
 chmod 755 generate.pe
./generate.pe *.sfd

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog

* Sat Feb 05 2022 22:56:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.2-1
- bumped upstream to version 3.0.2 
- change docs and licence to match upstream
- removed forgemeta references 

* Thu Feb 03 2022 19:36:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-4
- Modified fontconfig
- removed excess white spaces and tabs  in spec file
- modified source line and fontcofiglines in spec 

* Thu Feb 03 2022 15:30:00 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-3
- Preparing fonts from source sfd files using fontforge as required in gpl
- collecting source from remote 

* Wed Feb 02 2022 21:30:16 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-2
- modification of spec file to remove unecessary elements 

* Fri Jan 28 2022 21:42:16 +0530  Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-1
- Change in EM square from 2048 to 1000
- Upgrade fto Unicode 14.0 standard for Bengali
- shift from version 1 to version 2 of Bengali OpenType specification
- support for Assamese language
- support for both traditional and modern form of conjunts 
- addition of vedic stress marks
- removal of Latin glyphs
- removal of references and over lapping 
- addition of missing conjuncts 
- various bugfixes 
- Removed Bengali namespace error of double utf-8 encoding
- Created Mukti from MuktiNarrow 
- Converted splines from quadratic to cubic
- saved source in fontforge sfd format 
- removed microsoft volt tables from font  