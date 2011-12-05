Summary: UNIX to DOS text file format converter
Name: unix2dos
Version: 2.2
Release: 35%{?dist}
License: BSD
Group: Applications/Text
Source: unix2dos-2.2.src.tar.gz
Patch0: unix2dos-mkstemp.patch
Patch1: unix2dos-2.2-segfault.patch
Patch2: unix2dos-2.2-manpage.patch
Patch3: unix2dos-2.2-mode.patch
Patch4: unix2dos-2.2-tmppath.patch
Patch5: unix2dos-preserve-file-modes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%prep
%setup -q -c
# Use mkstemp.
%patch0 -p1 -b .sec

# Check for errors when creating temporary file.
%patch1 -p1 -b .segf

# Manual page fixes.
%patch2 -p1 -b .man

# Preserve file modes when converting in-place.
%patch3 -p1 -b .mode

# Don't just delete original file.
%patch4 -p1 -b .tmppath

# Preserve file modes when creating new file.
%patch5 -p1 -b .preserve-file-modes
perl -pi -e "s/^#endif.*/#endif/g;s/^#else.*/#else/g" *.[ch]

%description
A utility that converts plain text files in UNIX format to DOS format.

%build
gcc $RPM_OPT_FLAGS -o unix2dos unix2dos.c

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p -m755 unix2dos $RPM_BUILD_ROOT%{_bindir}
install -p -m444 unix2dos.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,0755)
%doc COPYRIGHT
%{_bindir}/unix2dos
%{_mandir}/*/*


%changelog
* Wed Mar  3 2010 Tim Waugh <twaugh@redhat.com> - 2.2-35
- Added comments for all patches.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.2-34.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.2-32
- fix license tag

* Mon Sep  8 2008 Tim Waugh <twaugh@redhat.com> 2.2-31
- Removed patch fuzz.
- Preserve file modes (bug #437469).
- Fixed grammar in man page (bug #460731).
- Explicitly apply patch0.

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 2.2-30
- Rebuild for GCC 4.3.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 2.2-29
- Rebuilt.

* Wed Feb  7 2007 Tim Waugh <twaugh@redhat.com> 2.2-28
- Fixed license tag (bug #226514).

* Tue Feb  6 2007 Tim Waugh <twaugh@redhat.com> 2.2-27
- Preserve timestamps on install (bug #226514).
- Fixed summary (bug #226514).
- Fixed build root (bug #226514).
- Don't explicitly require perl for build (bug #226514).
- Added dist to release tag (bug #226514).
- Don't build with '-Wall' since RPM_OPT_FLAGS already includes it
  (bug #226514).
- Fixed macros in changelog (bug #226514).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.2-26.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2-26.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2-26.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Apr 13 2005 Tim Waugh <twaugh@redhat.com>
- Merge last fix into tmppath patch, which introduced the original problem.

* Tue Apr 12 2005 Tim Waugh <twaugh@redhat.com> 2.2-26
- Removed inappropriate strcpy (bug #153079).  Patch from Neil Horman.

* Thu Mar  3 2005 Mike A. Harris <mharris@redhat.com> 2.2-25
- Rebuild with gcc 4 for FC4

* Wed Oct 20 2004 Miloslav Trmac <mitr@redhat.com> 2.2-24
- Don't just delete the original file when destination and current directory
  are on different filesystems 

* Mon Oct 11 2004 Tim Waugh <twaugh@redhat.com> 2.2-23
- Apply H J Lu's patch to preserve file mode (bug #91332).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Oct  7 2002 Mike A. Harris <mharris@redhat.com> 2.2-18
- All-arch rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Mar  5 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-15
- rebuild

* Thu Jan 17 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-14
- Fix up the mkstemp patch, don't segfault with lacking write permissions
  (#57700)
- Fix up man page (part 2 of #57700)
- Fix compiler warnings

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Nov 17 2000 Tim Powers <timp@redhat.com>
- patched to use mkstemp, not much had to be done.

* Thu Nov 16 2000 Tim Powers <timp@redhat.com>
- minor spec file cleanups
- built for 7.1
- use predefined RPM macros whenever possible
- use RPM_OPT_FLAGS when building

* Tue Jul 07 1999 Peter Soos <sp@osb.hu> 
- Added Hungarian "Summary:" and "%%description" 
- Corrected the file and directory attributes to rebuild the package 
  under RedHat Linux 6.0 
 
* Thu Jul 09 1998 Arkadiusz Mikkkkkkiewicz <misiek@misiek.eu.org> 
- Recompiled under RedHat Linux 5.1 
- Small changes in %%build and %%files 
- Added "Vendor:" 
- Added Polish "Summary:" and "%%description" 
 
* Thu Jun 18 1998 Peter Soos <sp@osb.hu> 
- Corrected the spec file for rpm 2.5 
 
* Fri Dec 5 1997 Peter Soos <sp@osb.hu> 
- Recompiled under RedHat Linux 5.0
