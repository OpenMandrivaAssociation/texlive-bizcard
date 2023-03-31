Name:		texlive-bizcard
Version:	15878
Release:	2
Summary:	Typeset business cards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bizcard
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an adaption for current LaTeX of a LaTeX 2.09 style by
Silvano Balemi. It produces cards at the normal US card size,
76.2mm x 50.8mm.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
