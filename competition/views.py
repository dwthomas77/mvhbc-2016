from itertools import chain
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from competition.forms import UserForm, JudgeUserForm, ProfileForm, AccountUserProfileForm, AddressForm, ProfileJudgeForm, SubmissionForm
from competition.models import UserProfile, Address, Submission, JudgingTable, Style

def process_login(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        return redirect('account')

def compWelcome(request):
    if request.method == 'POST':
        userData = {
            'username':  request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        # set and validate user form data
        userForm = UserForm(userData)
        if userForm.is_valid():
            addressForm = AddressForm()
            userProfileForm = ProfileForm()
            u = userForm.save()
            up = UserProfile(user=u)
            up.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return redirect('account')
                else:
                    return render(request, "competition/registration.html", {'userForm': userForm})
            else:
                return redirect('register')
        else:
            return render(request, 'competition/comp-welcome.html', {
                'userForm' : userForm
            })
    else:
        userForm = UserForm()
        return render(request, "competition/comp-welcome.html", {'userForm': userForm})

def registration(request):
    if request.method == 'POST':
        userData = {
            'username':  request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        # set and validate user form data
        myUserForm = UserForm(userData)
        if myUserForm.is_valid():
            return render(request, "competition/registration.html", {})
        else:
            return render(request, "competition/registration-error.html", {})
    else:
        return render(request, "competition/registration-error.html", {})

# User Registration
def register(request):
    if request.method == 'POST':
        userData = {
            'username':  request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        addressData = {
            'street_1' : request.POST['street_1'],
            'street_2' : request.POST['street_2'],
            'city' : request.POST['city'],
            'state' : request.POST['state'],
            'zipcode' : request.POST['zipcode']
        }
        profileData = {
            'club' : request.POST['club'],
            'aha_id' : request.POST['aha_id']
        }
        profileJudgeData = {
            'judge_preference' : request.POST['judge_preference'],
            'qualification' : request.POST['qualification'],
            'bjcp_registration' : request.POST['bjcp_registration'],
            'judge_comments' : request.POST['judge_comments']
        }
        # set and validate user form data
        userForm = UserForm(userData)
        addressForm = AddressForm(addressData)
        profileForm = ProfileForm(profileData)
        pJudgeForm = ProfileJudgeForm(profileJudgeData)
        if userForm.is_valid() and addressForm.is_valid():
            u = userForm.save()
            a = addressForm.save()
            profile = UserProfile(
                user=u,
                address=a,
                judge_preference = request.POST['judge_preference'],
                qualification = request.POST['qualification'],
                bjcp_registration = request.POST['bjcp_registration'],
                judge_comments = request.POST['judge_comments'],
                club = request.POST['club'],
                aha_id = request.POST['aha_id']
            )
            profile.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return redirect('account')
                else:
                    return render(request, "competition/registration.html", {'userForm': userForm, 'judgeForm': profileForm})
            else:
                return redirect('register')
        else:
            return render(request, 'competition/registration.html', {
                'userForm' : userForm,
                'addressForm' : addressForm,
                'profileForm' : profileForm,
                'pJudgeForm' : pJudgeForm
            })
    else:
        myUserForm = UserForm()
        addressForm = AddressForm()
        profileForm = ProfileForm()
        pJudgeForm = ProfileJudgeForm()
        return render(request, "competition/registration.html", {
            'userForm' : myUserForm,
            'addressForm' : addressForm,
            'profileForm' : profileForm,
            'pJudgeForm' : pJudgeForm
        })

# Judge Registration
def judge_register(request):
    if request.method == 'POST':
        userData = {
            'username':  request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        profileData = {
            'judge_preference' : request.POST['judge_preference'],
            'qualification' : request.POST['qualification'],
            'bjcp_registration' : request.POST['bjcp_registration'],
            'judge_comments' : request.POST['judge_comments'],
            'phone_number' : request.POST['phone_number'],
            'club' : request.POST['club'],
            'aha_id' : request.POST['aha_id']
        }
        # set and validate user form data
        userForm = UserForm(userData)
        profileForm = JudgeUserForm(profileData)
        if userForm.is_valid():
            u = userForm.save()
            profile = UserProfile(
                user=u,
                judge_preference = request.POST['judge_preference'],
                qualification = request.POST['qualification'],
                bjcp_registration = request.POST['bjcp_registration'],
                judge_comments = request.POST['judge_comments'],
                phone_number = request.POST['phone_number'],
                club = request.POST['club'],
                aha_id = request.POST['aha_id']
            )
            profile.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return redirect('j_account')
                else:
                    return render(request, "competition/judge-registration.html", {'userForm': userForm, 'judgeForm': profileForm})
            else:
                return redirect('judge_register')
        else:
            return render(request, 'competition/judge-registration.html', {
                'userForm' : userForm,
                'judgeForm' : profileForm
            })
    else:
        myUserForm = UserForm()
        judgeForm = JudgeUserForm()
        return render(request, "competition/judge-registration.html", {
            'userForm' : myUserForm,
            'judgeForm' : judgeForm
        })

# Account Page
def account(request):
    if not request.user.is_authenticated():
        return redirect('login')
    elif not hasattr(request.user, 'userprofile'):
        return redirect('login')
    elif not hasattr(request.user.userprofile.address, 'street_1'):
        return redirect('address_page')
    else:
        profile = request.user.userprofile
        # build forms
        userData = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'club': profile.club,
            'aha_id': profile.aha_id
        }
        userForm = AccountUserProfileForm(userData)
        addressForm = AddressForm(instance=profile.address)
        submissionForm = SubmissionForm()
        judgeForm = ProfileJudgeForm({
             'judge_preference' : profile.judge_preference,
             'qualification' : profile.qualification,
             'judge_comments' : profile.judge_comments,
             'bjcp_registration' : profile.bjcp_registration,

        })
        # query user submissions
        submission_query = Submission.objects.filter(brewer = profile)
        return render(request, "competition/account.html", {
            'userForm': userForm,
            'addressForm': addressForm,
            'judgeForm': judgeForm,
            'submissionForm': submissionForm,
            'entries': submission_query
        })

# Account Page
def j_account(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        if request.method == 'POST':
            # retrieve user profile
            profile = request.user.userprofile
            # set fields
            profile.judge_preference = request.POST['judge_preference']
            profile.qualification = request.POST['qualification']
            profile.judge_comments = request.POST['judge_comments']
            profile.bjcp_registration = request.POST['bjcp_registration']
            profile.phone_number = request.POST['phone_number']
            profile.club = request.POST['club']
            profile.aha_id = request.POST['aha_id']
            # save changes
            profile.save();
            # return updated model form
            judgeForm = JudgeUserForm({
                'judge_preference' : profile.judge_preference,
                'qualification' : profile.qualification,
                'judge_comments' : profile.judge_comments,
                'bjcp_registration' : profile.bjcp_registration,
                'phone_number' : profile.phone_number,
                'club' : profile.club,
                'aha_id' : profile.aha_id
            })
            return render(request, "competition/j_account.html", {
                'judgeForm': judgeForm
            })
        else:
            userForm = UserForm(request.user)
            profile = request.user.userprofile
            judgeForm = JudgeUserForm({
                'judge_preference' : profile.judge_preference,
                'qualification' : profile.qualification,
                'judge_comments' : profile.judge_comments,
                'bjcp_registration' : profile.bjcp_registration,
                'phone_number' : profile.phone_number,
                'club' : profile.club,
                'aha_id' : profile.aha_id
            })
            return render(request, "competition/j_account.html", {
                'judgeForm': judgeForm
            })

## UPDATES

def update_address(request):
    if not request.user.is_authenticated():
        return redirect('login')
    elif request.method == 'POST' and request.user.userprofile:
        profile = request.user.userprofile
        # build address form
        addressData = {
            'street_1': request.POST['street_1'],
            'street_2': request.POST['street_2'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'zipcode': request.POST['zipcode']
        }
        addressForm = AddressForm(addressData)
        if addressForm.is_valid():
            # save address
            a = profile.address
            a.street_1 = request.POST['street_1']
            a.street_2 = request.POST['street_2']
            a.city = request.POST['city']
            a.state = request.POST['state']
            a.zipcode = request.POST['zipcode']
            a.save()
            msg = "Address Successfully Updated"
        else:
            msg = "There was a problem with updating your address"
        # build other forms
        userData = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'club': profile.club,
            'aha_id': profile.aha_id
        }
        userForm = AccountUserProfileForm(userData)
        submissionForm = SubmissionForm()
        judgeForm = ProfileJudgeForm({
            'judge_preference' : profile.judge_preference,
            'qualification' : profile.qualification,
            'judge_comments' : profile.judge_comments,
            'bjcp_registration' : profile.bjcp_registration
        })
        # query user submissions
        submission_query = Submission.objects.filter(brewer = profile)
        return render(request, "competition/account.html", {
            'userForm': userForm,
            'addressForm': addressForm,
            'judgeForm': judgeForm,
            'submissionForm': submissionForm,
            'entries': submission_query,
            'infoMsg'   : msg
        })
    else:
        return redirect('account')

def update_profile(request):
    if not request.user.is_authenticated():
        return redirect('login')
    elif request.method == 'POST' and request.user.userprofile:
        profile = request.user.userprofile
        # build user form
        userForm = AccountUserProfileForm(request.POST)
        if userForm.is_valid():
            # save form fields
            request.user.first_name = request.POST['first_name']
            request.user.last_name = request.POST['last_name']
            request.user.email = request.POST['email']
            request.user.save()
            profile.club = request.POST['club']
            profile.aha_id = request.POST['aha_id']
            profile.save()
            msg = "User Profile Successfully Updated"
        else:
            msg = "There was a problem updating your User Profile"
        # build other forms
        addressForm = AddressForm(instance=profile.address)
        submissionForm = SubmissionForm()
        judgeForm = ProfileJudgeForm({
            'judge_preference' : profile.judge_preference,
            'qualification' : profile.qualification,
            'judge_comments' : profile.judge_comments,
            'bjcp_registration' : profile.bjcp_registration
        })
        # query user submissions
        submission_query = Submission.objects.filter(brewer = profile)
        return render(request, "competition/account.html", {
            'userForm': userForm,
            'addressForm': addressForm,
            'judgeForm': judgeForm,
            'submissionForm': submissionForm,
            'entries': submission_query,
            'infoMsg'   : msg
        })
    else:
        return redirect('account')

def update_judge(request):
    if not request.user.is_authenticated():
        return redirect('login')
    elif request.method == 'POST' and request.user.userprofile:
        profile = request.user.userprofile
        msg = "Judge Preferences have been updated"
        # set fields
        profile.judge_preference = request.POST['judge_preference']
        profile.qualification = request.POST['qualification']
        profile.judge_comments = request.POST['judge_comments']
        profile.bjcp_registration = request.POST['bjcp_registration']
        # save changes
        profile.save();
        # build other forms
        userData = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'club': profile.club,
            'aha_id': profile.aha_id
        }
        userForm = AccountUserProfileForm(userData)
        addressForm = AddressForm(instance=profile.address)
        submissionForm = SubmissionForm()
        judgeForm = ProfileJudgeForm({
            'judge_preference' : profile.judge_preference,
            'qualification' : profile.qualification,
            'judge_comments' : profile.judge_comments,
            'bjcp_registration' : profile.bjcp_registration
        })
        # query user submissions
        submission_query = Submission.objects.filter(brewer = profile)
        return render(request, "competition/account.html", {
            'userForm': userForm,
            'addressForm': addressForm,
            'judgeForm': judgeForm,
            'submissionForm': submissionForm,
            'entries': submission_query,
            'infoMsg'   : msg
        })
    else:
        return redirect('account')

## Add
def add_submission(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        if request.method == 'POST' and request.user.userprofile:
            profile = request.user.userprofile
            submission_data = {
                'style': request.POST['style'],
                'name': request.POST['name'],
                'comments': request.POST['comments']
            }
            submissionForm = SubmissionForm(submission_data)
            if submissionForm.is_valid():
                s = submissionForm.save(commit=False)
                s.brewer = profile
                s.save()
                styleId = str(s.style.style_id)
                submissionId = str(s.pk)
                s.competition_id = styleId + submissionId
                s.save()
                submissionForm = SubmissionForm()
                msg = "Submission successfully saved"
            else:
                msg = "There was a problem with your submission entry"
            #build forms
            userData = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'club': profile.club,
                'aha_id': profile.aha_id
            }
            userForm = AccountUserProfileForm(userData)
            addressForm = AddressForm(instance=profile.address)
            judgeForm = ProfileJudgeForm({
                'judge_preference' : profile.judge_preference,
                'qualification' : profile.qualification,
                'judge_comments' : profile.judge_comments,
                'bjcp_registration' : profile.bjcp_registration
            })
            # query user submissions
            submission_query = Submission.objects.filter(brewer = profile)
            return render(request, "competition/account.html", {
                'userForm': userForm,
                'addressForm': addressForm,
                'judgeForm': judgeForm,
                'submissionForm': submissionForm,
                'entries': submission_query,
                'infoMsg'   : msg
            })
        else:
            return redirect('login')

## Delete
def delete_submission(request, s_pk):
    if not request.user.is_authenticated():
        return redirect('register')
    else:
        # identify submission object and current user
        submission = get_object_or_404(Submission, pk=s_pk)
        profile = UserProfile.objects.get(pk=submission.brewer.pk)

        ## redirect if user is not owner of this submission or submission is not valid
        if (submission) and (request.user.userprofile != profile):
            return redirect('account')
        else:
            if request.method == 'POST':
                # delete submission
                submission.delete()
                #build forms
                userData = {
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'club': profile.club,
                    'aha_id': profile.aha_id
                }
                userForm = AccountUserProfileForm(userData)
                addressForm = AddressForm(instance=profile.address)
                submissionForm = SubmissionForm()
                judgeForm = ProfileJudgeForm({
                    'judge_preference' : profile.judge_preference,
                    'qualification' : profile.qualification,
                    'judge_comments' : profile.judge_comments,
                    'bjcp_registration' : profile.bjcp_registration
                })
                # query user submissions
                submission_query = Submission.objects.filter(brewer = profile)
                return render(request, "competition/account.html", {
                    'userForm': userForm,
                    'addressForm': addressForm,
                    'judgeForm': judgeForm,
                    'submissionForm': submissionForm,
                    'entries': submission_query,
                    'infoMsg'   : "Submission successfully deleted."
            })
            else:
                redirect('account')

## Address form for converting Judges to Users
def address_page(request):
    if not request.user.is_authenticated():
        return redirect('register')
    elif request.method == 'POST' and request.user.userprofile:
        profile = request.user.userprofile
        # build address form
        addressData = {
            'street_1': request.POST['street_1'],
            'street_2': request.POST['street_2'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'zipcode': request.POST['zipcode']
        }
        addressForm = AddressForm(addressData)
        if addressForm.is_valid():
            # save address
            a = addressForm.save()
            profile.address = a
            profile.save()
            return redirect('account')
        else:
            return render(request, "competition/address_form.html", {
                'addressForm': addressForm
            })
    else:
        addressForm = AddressForm()
        return render(request, "competition/address_form.html", {
            'addressForm': addressForm
        })

# # Tools0
@staff_member_required
def tools_home(request):
    return render(request, "competition/tools_home.html")

@staff_member_required
def table_manager(request):
    # Get All Dependency Objects from DB
    data = {
        'styles': Style.objects.all(),
        'users': UserProfile.objects.all(),
        'submissions': Submission.objects.all(),
        'tables': JudgingTable.objects.all(),
        'judges': UserProfile.objects.filter(judge_preference = 'Judge'),
        'stewards': UserProfile.objects.filter(judge_preference = 'Steward'),
    }
    return render(request, "competition/tools-table-manager.html", {'data': data})

@staff_member_required
def table_add(request):
        # get next table number
        next_table = str(JudgingTable.objects.count() + 1)
        next_table_name = "Table " + next_table
        # create new table
        table = JudgingTable(name=next_table_name)
        table.save()
        return redirect('table_manager');

@staff_member_required
def lock_category(request):
    if not request.user.is_authenticated():
        return redirect('register')
    elif request.method == 'POST':
        tableId = request.POST['tableId']
        categoryName = request.POST['categoryName']
        # get table
        table = JudgingTable.objects.get(pk=tableId);
        # get all Styles from this category
        style_set = Style.objects.filter(category = categoryName)
        for style in style_set:
            style.table = table
            style.save()
        return redirect('table_manager')
    else:
        return redirect('account')

# to unlock you must access the style through the table's table.style_set method
@staff_member_required
def unlock_category(request):
    if not request.user.is_authenticated():
        return redirect('register')
    elif request.method == 'POST':
        tableId = request.POST['tableId']
        categoryName = request.POST['categoryName']
        # get table
        table = JudgingTable.objects.get(pk=tableId);
        # get all Styles from this category
        style_set = Style.objects.filter(category = categoryName)
        # remove each style from the table
        for style in style_set:
            table.style_set.remove(style)
        return redirect('table_manager')
    else:
        return redirect('account')

@staff_member_required
def add_judge(request):
    if not request.user.is_authenticated():
        return redirect('register')
    elif request.method == 'POST':
        judgeId = request.POST['form-judgeAdd']
        tableId = request.POST['form-tableAddJudge']
        # get table
        table = JudgingTable.objects.get(pk=tableId)
        # get judge
        judge = UserProfile.objects.get(pk=judgeId)
        # add judge to table
        table.judges.add(judge)
        return redirect('table_manager')
    else:
        return redirect('account')

@staff_member_required
def add_steward(request):
    if not request.user.is_authenticated():
        return redirect('register')
    elif request.method == 'POST':
        stewardId = request.POST['form-stewardAdd']
        tableId = request.POST['form-tableAddSteward']
        # get table
        table = JudgingTable.objects.get(pk=tableId)
        # get steward
        steward = UserProfile.objects.get(pk=stewardId)
        # add steward to table
        table.stewards.add(steward)
        return redirect('table_manager')
    else:
        return redirect('account')

@staff_member_required
def remove_judge(request):
    if not request.user.is_authenticated():
        return redirect('register')
    elif request.method == 'POST':
        judgeId = request.POST['form-judgeRemove']
        tableId = request.POST['form-tableRemoveJudge']
        # get table
        table = JudgingTable.objects.get(pk=tableId)
        # get judge
        judge = UserProfile.objects.get(pk=judgeId)
        # add judge to table
        table.judges.remove(judge)
        return redirect('table_manager')
    else:
        return redirect('account')

@staff_member_required
def remove_steward(request):
    if not request.user.is_authenticated():
        return redirect('register')
    elif request.method == 'POST':
        stewardId = request.POST['form-stewardRemove']
        tableId = request.POST['form-tableRemoveSteward']
        # get table
        table = JudgingTable.objects.get(pk=tableId)
        # get steward
        steward = UserProfile.objects.get(pk=stewardId)
        # add steward to table
        table.stewards.remove(steward)
        return redirect('table_manager')
    else:
        return redirect('account')

@staff_member_required
def view_judges(request):
    # Get All Dependency Objects from DB
    data = {
        'styles': Style.objects.all(),
        'users': UserProfile.objects.all(),
        'submissions': Submission.objects.all(),
        'tables': JudgingTable.objects.all(),
        'judges': UserProfile.objects.filter(judge_preference = 'Judge'),
        'stewards': UserProfile.objects.filter(judge_preference = 'Steward'),
    }
    return render(request, "competition/view_judges.html", {'data':data})

@staff_member_required
def view_submissions(request):
    # Get All Dependency Objects from DB
    data = {
        'styles': Style.objects.all(),
        'users': UserProfile.objects.all(),
        'submissions': Submission.objects.all(),
        'tables': JudgingTable.objects.all(),
        'judges': UserProfile.objects.filter(judge_preference = 'Judge'),
        'stewards': UserProfile.objects.filter(judge_preference = 'Steward'),
    }
    return render(request, "competition/view_submissions.html", {'data':data})

@staff_member_required
def view_brewers(request):
    # Get All Dependency Objects from DB
    data = {
        'styles': Style.objects.all(),
        'users': UserProfile.objects.all(),
        'submissions': Submission.objects.all(),
        'tables': JudgingTable.objects.all(),
        'judges': UserProfile.objects.filter(judge_preference = 'Judge'),
        'stewards': UserProfile.objects.filter(judge_preference = 'Steward'),
        'brewers': UserProfile.objects.all()
    }
    for u in data['brewers']:
        u.submissions = Submission.objects.filter(brewer = u)
    return render(request, "competition/view_brewers.html", {'data':data})

@staff_member_required
def switch_table(request):
    tableId = request.POST['switchTableId']
    # get table
    table = JudgingTable.objects.get(pk=tableId)
    # switch sessions
    if table.session == 'AM':
        table.session = 'PM'
    else:
        table.session = 'AM'
    table.save()
    return redirect('table_manager')

@staff_member_required
def pull_sheet(request, pk):
    table = get_object_or_404(JudgingTable, pk=pk)
    styles = table.style_set.all()
    submissions = []
    for style in styles:
        submissions = list(chain(submissions, style.submission_set.all()))

    return render(request, "competition/pullsheet.html", {
        'table':table,
        'styles':styles,
        'submissions':submissions
    })

@staff_member_required
def table_score(request, pk):
    table = get_object_or_404(JudgingTable, pk=pk)
    styles = table.style_set.all()
    submissions = []
    for style in styles:
        submissions = list(chain(submissions, style.submission_set.all()))

    return render(request, "competition/table_score.html", {
        'table':table,
        'styles':styles,
        'submissions':submissions
    })

@staff_member_required
def table_score_post(request, pk):
    return redirect('table_manager')

def print_label(request, e_pk):
    e = get_object_or_404(Submission, pk=e_pk)
    return render(request, "competition/print_label.html", {'entry':e})

def results_2015(request):
    return render(request, "competition/results_2015.html")

def results_2014(request):
    return render(request, "competition/results_2014.html")

def results_2013(request):
    return render(request, "competition/results_2013.html")

def results_2012(request):
    return render(request, "competition/results_2012.html")

def sponsors(request):
    return render(request, "competition/sponsors.html")

def locations(request):
    return render(request, "competition/competition-locations.html")

def info(request):
    return render(request, "competition/competition-info.html")
