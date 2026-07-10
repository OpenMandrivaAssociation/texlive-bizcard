%global tl_name bizcard
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Typeset business cards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bizcard
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an adaption for current LaTeX of a LaTeX 2.09 style by Silvano
Balemi. It produces cards at the normal US card size, 76.2mm x 50.8mm.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bizcard
%dir %{_datadir}/texmf-dist/source/latex/bizcard
%dir %{_datadir}/texmf-dist/tex/latex/bizcard
%doc %{_datadir}/texmf-dist/doc/latex/bizcard/bizcard.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bizcard/bizex.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bizcard/bizex.tex
%doc %{_datadir}/texmf-dist/source/latex/bizcard/bizcard.drv
%doc %{_datadir}/texmf-dist/source/latex/bizcard/bizcard.dtx
%doc %{_datadir}/texmf-dist/source/latex/bizcard/bizcard.ins
%{_datadir}/texmf-dist/tex/latex/bizcard/bizcard.sty
