# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bizcard
# catalog-date 2009-04-30 00:32:08 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-bizcard
Version:	1.1
Release:	1
Summary:	Typeset business cards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bizcard
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is an adaption for current LaTeX of a LaTeX 2.09 style by
Silvano Balemi. It produces cards at the normal US card size,
76.2mm x 50.8mm.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bizcard/bizcard.sty
%doc %{_texmfdistdir}/doc/latex/bizcard/bizcard.pdf
%doc %{_texmfdistdir}/doc/latex/bizcard/bizex.pdf
%doc %{_texmfdistdir}/doc/latex/bizcard/bizex.tex
#- source
%doc %{_texmfdistdir}/source/latex/bizcard/bizcard.drv
%doc %{_texmfdistdir}/source/latex/bizcard/bizcard.dtx
%doc %{_texmfdistdir}/source/latex/bizcard/bizcard.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
