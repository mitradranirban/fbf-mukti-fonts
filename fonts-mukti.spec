# SPDX-License-Identifqier: MIT
	

	
 %global  fontfamily mukti
Version:   3.0.1
	
Release:   1
	
URL:       https://github.com/mitradranirban/fonts-mukti
	
	
%global foundry fbf  
	
%global fontlicense       GPl3+FontException
	
	
%global fontlicenses      LICENCE.txt
	
	
%global fontdocs          *.txt
	
%global fontdocsex        %{fontlicenses}
	
%global fontfamily0        Mukti
	
%global fontsummary0      Popular GPLed Bengali OpenType  font 
	
%global fonts0            *.otf
	
%global fontconfs0        %{_sourcedir}/fbf-mukti-fonts-3.0.1/67-font-mukti.conf
	
	
%global fontdescription0  %{expand:
This is a one of the earliest Open Source OpenType Bengali / Bangla font It was made by using good quality glyphs of GPLed font bng2-n from Cyberscape Multimedia 
<https://web.archive.org/web/20021113130716/http://www.akruti.com/freedom/>. It was made for Mukta Bangla Font project.
	
}
	
 %fontpkg fbf-mukti-fonts
	
%sourcelist
	
 
	
%foundry-%fontfamily-fonts-%version.tar.gz
 	
 
	
%prep
	
%setup
	
	
%build
	
%fontbuild
	
	
%install
	
%fontinstall
	
	
%check
	
%fontcheck
	
	
%fontfiles
	
	
%changelog

* Fri Jan 28 2022 21:42:16 +0530  Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1
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
* Wed Sep 19 2018 20:02:43 +0530  Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 2.1.0
- added Open type tables to font
* Tue Nov 10 2015 07:16:51 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 2.0.0
- Removed Bengali namespace error of double utf-8 encoding
* Thu Jan 26 2006 +00:00:00 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 1.9.9
- Created Mukti from MuktiNarrow 
- Converted splines from quadratic to cubic
- saved source in fontforge sfd format 
- removed microsoft volt tables from font  
 


