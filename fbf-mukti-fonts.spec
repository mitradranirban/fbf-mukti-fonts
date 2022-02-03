# SPDX-License-Identifqier: MIT


Version:   3.0.1
	
Release:   3
	
URL:       https://github.com/mitradranirban/fbf-mukti-fonts

Source0: https://github.com/mitradranirban/fbf-mukti-fonts/blob/main/fbf-mukti-fonts-3.0.1.tar.gz
Source1: https://github.com/mitradranirban/fbf-mukti-fonts/blob/main/65-0-fbf-mukti-fonts.conf
	
%global foundry fbf 
  
%global fontfamily    mukti         

%global fontlicense       GPlv3+ with exception
	
%global fontlicenses      LICENCE.txt
	
%global fontdocs          *.txt
	
%global fontdocsex        %{fontlicenses}
	
%global fontsummary      Popular GPLed Bengali OpenType  font 
	
%global fonts            *.otf
	
%global fontconfs        %{Source1}

BuildArch:      noarch

BuildRequires: fontforge 
	
 
%global fontdescription  %{expand:
This is a one of the earliest Open Source OpenType Bengali / Bangla font It was made by using good quality glyphs of GPLed font bng2-n from Cyberscape Multimedia 
<https://web.archive.org/web/20021113130716/http://www.akruti.com/freedom/>. It was made for Mukta Bangla Font project.
	
}
	
 
	
%fontpkg 


%sourcelist
	
 
	
%prep

%setup

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
 

