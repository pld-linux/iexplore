# This spec file is released under the GNU General Public License version 2.0
# (http://www.gnu.org/licenses/gpl.txt).
#
# NOTE: Releasing this spec file under the GPL does not alter the licensing
# of Internet Explorer itself. Satisfying the terms of Internet Explorer's
# license remains the user's responsibility.

%define	ver	5.5SP1
%define	rel	1
%define _wine_cdrive    %{_datadir}/wine
%define _wine_system    %{_wine_cdrive}/windows/system
%define _wine_programs  %{_wine_cdrive}/'Program Files'
%define _installdir     %{_wine_programs}/'Internet Explorer'

Summary:	Microsoft Internet Explorer 5.5SP1
Name:		iexplore
ExclusiveArch:	%{ix86}
Version:	%ver
Release:	%rel
Vendor:		Microsoft
Source0:	http://mirror.aarnet.edu.au/pub/microsoft/internet-explorer/5.5sp1/win9x/ie55sp1.exe
Source1:	http://www.james.id.au/specfiles/%{name}-supplementary.tar.bz2
Requires:	wine, wine-utils, dcom98
BuildRequires:	wine, cabextract, unzip, util-linux
Group:		Networking/WWW
######		Unknown group!
License:	Proprietary
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Url:		http://www.microsoft.com/windows/ie/support/ie55exsupport.asp

%description
The private, reliable, and flexible internet browsing experience.

%prep
mkdir $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
# unpack the insstaller file.
unzip -LL $RPM_SOURCE_DIR/ie55sp1.exe
# unpack config, registry etc.
tar xjvf $RPM_SOURCE_DIR/iexplore-supplementary.tar.bz2

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
mkdir tmp
# pull out the files with interesting stuff in them.
mv "ie 5.5 sp1 full"/ie_s*.cab tmp/
mv "ie 5.5 sp1 full"/iemil_3.cab tmp/
rm -rf "ie 5.5 sp1 full"
cd tmp
cabextract -L ie_s*
rm -f ie_s*
# work around a cabextract bug:
mkdir files
rename .cab .CAB ie_*.cab
cabextract -d files -L ie_*.CAB
cabextract -d files -L iemil_3.cab
rm -f *.CAB *.cab
# put the files in their final positions
install -d $RPM_BUILD_ROOT/%{_installdir}
install -d $RPM_BUILD_ROOT/%{_wine_system}
cd files
mv iexplore.exe $RPM_BUILD_ROOT/%{_installdir}
mv * $RPM_BUILD_ROOT/%{_wine_system}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iexplore
%{_datadir}/iexplore/config
%{_datadir}/iexplore/system.reg
%{_prefix}/wine/Program*/Internet*/iexplore.exe
%{_wine_system}/actxprxy.dll
%{_wine_system}/apps.hlp
%{_wine_system}/atl.dll
%{_wine_system}/bindfile.dll
%{_wine_system}/browselc.dll
%{_wine_system}/browseui.dll
%{_wine_system}/certmgr.msc
%{_wine_system}/ckcnv.exe
%{_wine_system}/corpol.dll
%{_wine_system}/crypt32.dll
%{_wine_system}/cryptdlg.dll
%{_wine_system}/cryptext.dll
%{_wine_system}/cryptnet.dll
%{_wine_system}/cryptui.dll
%{_wine_system}/deliebak.inf
%{_wine_system}/dhtmled.ocx
%{_wine_system}/digest.dll
%{_wine_system}/dispex.dll
%{_wine_system}/dssbase.dll
%{_wine_system}/dsssig.exe
%{_wine_system}/dxtmsft.dll
%{_wine_system}/dxtrans.dll
%{_wine_system}/enhsig.dll
%{_wine_system}/extrac32.exe
%{_wine_system}/fixie.inf
%{_wine_system}/hlink.dll
%{_wine_system}/hmmapi.dll
%{_wine_system}/html32.cnv
%{_wine_system}/ie4uinit.exe
%{_wine_system}/iedkcs32.dll
%{_wine_system}/iefiles5.inf
%{_wine_system}/ieinfo5.mof
%{_wine_system}/ieinfo5.ocx
%{_wine_system}/iejit.htm
%{_wine_system}/iepeers.dll
%{_wine_system}/iernonce.dll
%{_wine_system}/iesetup.dll
%{_wine_system}/ie.txt
%{_wine_system}/ieuinit.inf
%{_wine_system}/imgutil.dll
%{_wine_system}/inetcplc.dll
%{_wine_system}/inetcpl.cpl
%{_wine_system}/initpki.dll
%{_wine_system}/inseng.dll
%{_wine_system}/instrsa.dll
%{_wine_system}/instsch.dll
%{_wine_system}/jitalert.gif
%{_wine_system}/jobexec.dll
%{_wine_system}/jscript.dll
%{_wine_system}/license.txt
%{_wine_system}/loadwc.exe
%{_wine_system}/migrate.dll
%{_wine_system}/mlang.dll
%{_wine_system}/mmutilse.dll
%{_wine_system}/mscat32.dll
%{_wine_system}/msconv97.dll
%{_wine_system}/msdatsrc.tlb
%{_wine_system}/msencode.dll
%{_wine_system}/mshta.exe
%{_wine_system}/mshtml.dll
%{_wine_system}/mshtmled.dll
%{_wine_system}/mshtmler.dll
%{_wine_system}/mshtml.tlb
%{_wine_system}/msls31.dll
%{_wine_system}/msnauth.cnt
%{_wine_system}/msnauth.hlp
%{_wine_system}/msnsspc.dll
%{_wine_system}/msoss.dll
%{_wine_system}/msrating.dll
%{_wine_system}/mssign32.dll
%{_wine_system}/mssip32.dll
%{_wine_system}/mstime.dll
%{_wine_system}/msxml.dll
%{_wine_system}/occache.dll
%{_wine_system}/pingname.bat
%{_wine_system}/pingnum.bat
%{_wine_system}/plugin.ocx
%{_wine_system}/proctexe.ocx
%{_wine_system}/psbase.dll
%{_wine_system}/pstorec.dll
%{_wine_system}/pstorerc.dll
%{_wine_system}/pstores.exe
%{_wine_system}/ratings.chm
%{_wine_system}/ratings.cnt
%{_wine_system}/ratings.hlp
%{_wine_system}/related.htm
%{_wine_system}/removbak.inf
%{_wine_system}/rsabase.dll
%{_wine_system}/rsaci.rat
%{_wine_system}/rsasig.dll
%{_wine_system}/schannel.dll
%{_wine_system}/scrobj.dll
%{_wine_system}/secauth.hlp
%{_wine_system}/sendmail.dll
%{_wine_system}/setupwbv.dll
%{_wine_system}/shd401lc.dll
%{_wine_system}/shdoc401.dll
%{_wine_system}/shdoclc.dll
%{_wine_system}/shdocvw.dll
%{_wine_system}/shfolder.dll
%{_wine_system}/shlwapi.dll
%{_wine_system}/signin.hlp
%{_wine_system}/simpdata.tlb
%{_wine_system}/softpub.dll
%{_wine_system}/start.wav
%{_wine_system}/support.txt
%{_wine_system}/thumbvw.dll
%{_wine_system}/tip.htm
%{_wine_system}/tips.gif
%{_wine_system}/triedit.dll
%{_wine_system}/url.dll
%{_wine_system}/urlmon.dll
%{_wine_system}/userstub.exe
%{_wine_system}/w2kexcp.exe
%{_wine_system}/wallpapr.htm
%{_wine_system}/wininet.dll
%{_wine_system}/wintrust.dll
%{_wine_system}/wldap32.dll
%{_wine_system}/xenroll.dll
