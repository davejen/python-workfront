# generated from https://api-cl01.attask-ondemand.com/attask/api/v4.0/metadata
from ..meta import APIVersion, Object, Field, Reference, Collection

api = APIVersion('v4.0')


class AccessRule(Object):
    code = 'ACSRUL'
    accessor_id = Field('accessorID')
    accessor_obj_code = Field('accessorObjCode')
    ancestor_id = Field('ancestorID')
    ancestor_obj_code = Field('ancestorObjCode')
    core_action = Field('coreAction')
    customer_id = Field('customerID')
    forbidden_actions = Field('forbiddenActions')
    is_inherited = Field('isInherited')
    secondary_actions = Field('secondaryActions')
    security_obj_code = Field('securityObjCode')
    security_obj_id = Field('securityObjID')
    customer = Reference('customer')

api.register(AccessRule)


class Approval(Object):
    code = 'APPROVAL'
    bccompletion_state = Field('BCCompletionState')
    url = Field('URL')
    actual_benefit = Field('actualBenefit')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration = Field('actualDuration')
    actual_duration_expression = Field('actualDurationExpression')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_expense_cost = Field('actualExpenseCost')
    actual_hours_last_month = Field('actualHoursLastMonth')
    actual_hours_last_three_months = Field('actualHoursLastThreeMonths')
    actual_hours_this_month = Field('actualHoursThisMonth')
    actual_hours_two_months_ago = Field('actualHoursTwoMonthsAgo')
    actual_labor_cost = Field('actualLaborCost')
    actual_revenue = Field('actualRevenue')
    actual_risk_cost = Field('actualRiskCost')
    actual_start_date = Field('actualStartDate')
    actual_value = Field('actualValue')
    actual_work = Field('actualWork')
    actual_work_required = Field('actualWorkRequired')
    actual_work_required_expression = Field('actualWorkRequiredExpression')
    age_range_as_string = Field('ageRangeAsString')
    alignment = Field('alignment')
    alignment_score_card_id = Field('alignmentScoreCardID')
    all_approved_hours = Field('allApprovedHours')
    all_unapproved_hours = Field('allUnapprovedHours')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    assigned_to_id = Field('assignedToID')
    assignments_list_string = Field('assignmentsListString')
    audit_note = Field('auditNote')
    audit_types = Field('auditTypes')
    audit_user_ids = Field('auditUserIDs')
    auto_baseline_recur_on = Field('autoBaselineRecurOn')
    auto_baseline_recurrence_type = Field('autoBaselineRecurrenceType')
    auto_closure_date = Field('autoClosureDate')
    backlog_order = Field('backlogOrder')
    billed_revenue = Field('billedRevenue')
    billing_amount = Field('billingAmount')
    billing_record_id = Field('billingRecordID')
    budget = Field('budget')
    budget_status = Field('budgetStatus')
    budgeted_completion_date = Field('budgetedCompletionDate')
    budgeted_cost = Field('budgetedCost')
    budgeted_hours = Field('budgetedHours')
    budgeted_labor_cost = Field('budgetedLaborCost')
    budgeted_start_date = Field('budgetedStartDate')
    business_case_status_label = Field('businessCaseStatusLabel')
    can_start = Field('canStart')
    category_id = Field('categoryID')
    color = Field('color')
    commit_date = Field('commitDate')
    commit_date_range = Field('commitDateRange')
    company_id = Field('companyID')
    completion_pending_date = Field('completionPendingDate')
    completion_type = Field('completionType')
    condition = Field('condition')
    condition_type = Field('conditionType')
    constraint_date = Field('constraintDate')
    converted_op_task_entry_date = Field('convertedOpTaskEntryDate')
    converted_op_task_name = Field('convertedOpTaskName')
    converted_op_task_originator_id = Field('convertedOpTaskOriginatorID')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    cpi = Field('cpi')
    csi = Field('csi')
    currency = Field('currency')
    current_approval_step_id = Field('currentApprovalStepID')
    current_status_duration = Field('currentStatusDuration')
    customer_id = Field('customerID')
    days_late = Field('daysLate')
    deliverable_score_card_id = Field('deliverableScoreCardID')
    deliverable_success_score = Field('deliverableSuccessScore')
    deliverable_success_score_ratio = Field('deliverableSuccessScoreRatio')
    description = Field('description')
    display_order = Field('displayOrder')
    due_date = Field('dueDate')
    duration = Field('duration')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    eac = Field('eac')
    enable_auto_baselines = Field('enableAutoBaselines')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    estimate = Field('estimate')
    ext_ref_id = Field('extRefID')
    filter_hour_types = Field('filterHourTypes')
    finance_last_update_date = Field('financeLastUpdateDate')
    first_response = Field('firstResponse')
    fixed_cost = Field('fixedCost')
    fixed_end_date = Field('fixedEndDate')
    fixed_revenue = Field('fixedRevenue')
    fixed_start_date = Field('fixedStartDate')
    group_id = Field('groupID')
    handoff_date = Field('handoffDate')
    has_budget_conflict = Field('hasBudgetConflict')
    has_calc_error = Field('hasCalcError')
    has_completion_constraint = Field('hasCompletionConstraint')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_rate_override = Field('hasRateOverride')
    has_resolvables = Field('hasResolvables')
    has_start_constraint = Field('hasStartConstraint')
    has_timed_notifications = Field('hasTimedNotifications')
    hours_per_point = Field('hoursPerPoint')
    how_old = Field('howOld')
    indent = Field('indent')
    is_agile = Field('isAgile')
    is_complete = Field('isComplete')
    is_critical = Field('isCritical')
    is_duration_locked = Field('isDurationLocked')
    is_help_desk = Field('isHelpDesk')
    is_leveling_excluded = Field('isLevelingExcluded')
    is_ready = Field('isReady')
    is_work_required_locked = Field('isWorkRequiredLocked')
    iteration_id = Field('iterationID')
    last_calc_date = Field('lastCalcDate')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_mode = Field('levelingMode')
    leveling_start_delay = Field('levelingStartDelay')
    leveling_start_delay_expression = Field('levelingStartDelayExpression')
    leveling_start_delay_minutes = Field('levelingStartDelayMinutes')
    master_task_id = Field('masterTaskID')
    milestone_id = Field('milestoneID')
    milestone_path_id = Field('milestonePathID')
    name = Field('name')
    next_auto_baseline_date = Field('nextAutoBaselineDate')
    number_of_children = Field('numberOfChildren')
    number_open_op_tasks = Field('numberOpenOpTasks')
    olv = Field('olv')
    op_task_type = Field('opTaskType')
    op_task_type_label = Field('opTaskTypeLabel')
    optimization_score = Field('optimizationScore')
    original_duration = Field('originalDuration')
    original_work_required = Field('originalWorkRequired')
    owner_id = Field('ownerID')
    owner_privileges = Field('ownerPrivileges')
    parent_id = Field('parentID')
    parent_lag = Field('parentLag')
    parent_lag_type = Field('parentLagType')
    percent_complete = Field('percentComplete')
    performance_index_method = Field('performanceIndexMethod')
    personal = Field('personal')
    planned_benefit = Field('plannedBenefit')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_duration = Field('plannedDuration')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_risk_cost = Field('plannedRiskCost')
    planned_start_date = Field('plannedStartDate')
    planned_value = Field('plannedValue')
    pop_account_id = Field('popAccountID')
    portfolio_id = Field('portfolioID')
    portfolio_priority = Field('portfolioPriority')
    predecessor_expression = Field('predecessorExpression')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    program_id = Field('programID')
    progress_status = Field('progressStatus')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_duration_minutes = Field('projectedDurationMinutes')
    projected_start_date = Field('projectedStartDate')
    queue_def_id = Field('queueDefID')
    queue_topic_id = Field('queueTopicID')
    recurrence_number = Field('recurrenceNumber')
    recurrence_rule_id = Field('recurrenceRuleID')
    reference_number = Field('referenceNumber')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_cost = Field('remainingCost')
    remaining_duration_minutes = Field('remainingDurationMinutes')
    remaining_revenue = Field('remainingRevenue')
    remaining_risk_cost = Field('remainingRiskCost')
    reserved_time_id = Field('reservedTimeID')
    resolution_time = Field('resolutionTime')
    resolve_op_task_id = Field('resolveOpTaskID')
    resolve_project_id = Field('resolveProjectID')
    resolve_task_id = Field('resolveTaskID')
    resolving_obj_code = Field('resolvingObjCode')
    resolving_obj_id = Field('resolvingObjID')
    resource_pool_id = Field('resourcePoolID')
    resource_scope = Field('resourceScope')
    revenue_type = Field('revenueType')
    risk = Field('risk')
    risk_performance_index = Field('riskPerformanceIndex')
    roi = Field('roi')
    role_id = Field('roleID')
    schedule_id = Field('scheduleID')
    schedule_mode = Field('scheduleMode')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    selected_on_portfolio_optimizer = Field('selectedOnPortfolioOptimizer')
    severity = Field('severity')
    slack_date = Field('slackDate')
    source_obj_code = Field('sourceObjCode')
    source_obj_id = Field('sourceObjID')
    source_task_id = Field('sourceTaskID')
    spi = Field('spi')
    sponsor_id = Field('sponsorID')
    status = Field('status')
    status_equates_with = Field('statusEquatesWith')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    summary_completion_type = Field('summaryCompletionType')
    task_constraint = Field('taskConstraint')
    task_number = Field('taskNumber')
    task_number_predecessor_string = Field('taskNumberPredecessorString')
    team_id = Field('teamID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    total_hours = Field('totalHours')
    total_op_task_count = Field('totalOpTaskCount')
    total_task_count = Field('totalTaskCount')
    tracking_mode = Field('trackingMode')
    update_type = Field('updateType')
    url_ = Field('url')
    version = Field('version')
    wbs = Field('wbs')
    work = Field('work')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    work_unit = Field('workUnit')
    alignment_score_card = Reference('alignmentScoreCard')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    billing_record = Reference('billingRecord')
    category = Reference('category')
    company = Reference('company')
    converted_op_task_originator = Reference('convertedOpTaskOriginator')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    default_baseline = Reference('defaultBaseline')
    default_baseline_task = Reference('defaultBaselineTask')
    deliverable_score_card = Reference('deliverableScoreCard')
    entered_by = Reference('enteredBy')
    exchange_rate = Reference('exchangeRate')
    group = Reference('group')
    iteration = Reference('iteration')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone = Reference('milestone')
    milestone_path = Reference('milestonePath')
    owner = Reference('owner')
    parent = Reference('parent')
    portfolio = Reference('portfolio')
    primary_assignment = Reference('primaryAssignment')
    program = Reference('program')
    project = Reference('project')
    queue_def = Reference('queueDef')
    queue_topic = Reference('queueTopic')
    rejection_issue = Reference('rejectionIssue')
    reserved_time = Reference('reservedTime')
    resolve_op_task = Reference('resolveOpTask')
    resolve_project = Reference('resolveProject')
    resolve_task = Reference('resolveTask')
    resource_pool = Reference('resourcePool')
    role = Reference('role')
    schedule = Reference('schedule')
    source_task = Reference('sourceTask')
    sponsor = Reference('sponsor')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    template = Reference('template')
    template_task = Reference('templateTask')
    work_item = Reference('workItem')
    access_rules = Collection('accessRules')
    alignment_values = Collection('alignmentValues')
    all_hours = Collection('allHours')
    all_priorities = Collection('allPriorities')
    all_severities = Collection('allSeverities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    assignments = Collection('assignments')
    baselines = Collection('baselines')
    billing_records = Collection('billingRecords')
    children = Collection('children')
    deliverable_values = Collection('deliverableValues')
    documents = Collection('documents')
    done_statuses = Collection('doneStatuses')
    exchange_rates = Collection('exchangeRates')
    expenses = Collection('expenses')
    hour_types = Collection('hourTypes')
    hours = Collection('hours')
    op_tasks = Collection('opTasks')
    open_op_tasks = Collection('openOpTasks')
    predecessors = Collection('predecessors')
    project_user_roles = Collection('projectUserRoles')
    project_users = Collection('projectUsers')
    rates = Collection('rates')
    resolvables = Collection('resolvables')
    resource_allocations = Collection('resourceAllocations')
    risks = Collection('risks')
    roles = Collection('roles')
    routing_rules = Collection('routingRules')
    successors = Collection('successors')
    tasks = Collection('tasks')
    updates = Collection('updates')

api.register(Approval)


class ApprovalPath(Object):
    code = 'ARVPTH'
    approval_process_id = Field('approvalProcessID')
    customer_id = Field('customerID')
    duration_minutes = Field('durationMinutes')
    duration_unit = Field('durationUnit')
    rejected_status = Field('rejectedStatus')
    rejected_status_label = Field('rejectedStatusLabel')
    should_create_issue = Field('shouldCreateIssue')
    target_status = Field('targetStatus')
    target_status_label = Field('targetStatusLabel')
    approval_process = Reference('approvalProcess')
    customer = Reference('customer')
    approval_steps = Collection('approvalSteps')

api.register(ApprovalPath)


class ApprovalProcess(Object):
    code = 'ARVPRC'
    approval_obj_code = Field('approvalObjCode')
    approval_statuses = Field('approvalStatuses')
    customer_id = Field('customerID')
    description = Field('description')
    duration_minutes = Field('durationMinutes')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    is_private = Field('isPrivate')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    approval_paths = Collection('approvalPaths')

api.register(ApprovalProcess)


class ApprovalStep(Object):
    code = 'ARVSTP'
    approval_path_id = Field('approvalPathID')
    approval_type = Field('approvalType')
    customer_id = Field('customerID')
    name = Field('name')
    sequence_number = Field('sequenceNumber')
    approval_path = Reference('approvalPath')
    customer = Reference('customer')
    step_approvers = Collection('stepApprovers')

api.register(ApprovalStep)


class ApproverStatus(Object):
    code = 'ARVSTS'
    approvable_obj_code = Field('approvableObjCode')
    approvable_obj_id = Field('approvableObjID')
    approval_step_id = Field('approvalStepID')
    approved_by_id = Field('approvedByID')
    customer_id = Field('customerID')
    is_overridden = Field('isOverridden')
    op_task_id = Field('opTaskID')
    overridden_user_id = Field('overriddenUserID')
    project_id = Field('projectID')
    status = Field('status')
    step_approver_id = Field('stepApproverID')
    task_id = Field('taskID')
    wildcard_user_id = Field('wildcardUserID')
    approval_step = Reference('approvalStep')
    approved_by = Reference('approvedBy')
    customer = Reference('customer')
    op_task = Reference('opTask')
    overridden_user = Reference('overriddenUser')
    project = Reference('project')
    step_approver = Reference('stepApprover')
    task = Reference('task')
    wildcard_user = Reference('wildcardUser')

api.register(ApproverStatus)


class Assignment(Object):
    code = 'ASSGN'
    assigned_by_id = Field('assignedByID')
    assigned_to_id = Field('assignedToID')
    assignment_percent = Field('assignmentPercent')
    avg_work_per_day = Field('avgWorkPerDay')
    customer_id = Field('customerID')
    feedback_status = Field('feedbackStatus')
    is_primary = Field('isPrimary')
    is_team_assignment = Field('isTeamAssignment')
    op_task_id = Field('opTaskID')
    project_id = Field('projectID')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    status = Field('status')
    task_id = Field('taskID')
    team_id = Field('teamID')
    work = Field('work')
    work_required = Field('workRequired')
    work_unit = Field('workUnit')
    assigned_by = Reference('assignedBy')
    assigned_to = Reference('assignedTo')
    customer = Reference('customer')
    op_task = Reference('opTask')
    project = Reference('project')
    role = Reference('role')
    task = Reference('task')
    team = Reference('team')
    work_item = Reference('workItem')

api.register(Assignment)


class Avatar(Object):
    code = 'AVATAR'
    allowed_actions = Field('allowedActions')
    avatar_date = Field('avatarDate')
    avatar_download_url = Field('avatarDownloadURL')
    avatar_size = Field('avatarSize')
    avatar_x = Field('avatarX')
    avatar_y = Field('avatarY')
    handle = Field('handle')

api.register(Avatar)


class BackgroundJob(Object):
    code = 'BKGJOB'
    access_count = Field('accessCount')
    changed_objects = Field('changedObjects')
    customer_id = Field('customerID')
    end_date = Field('endDate')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    error_message = Field('errorMessage')
    expiration_date = Field('expirationDate')
    handler_class_name = Field('handlerClassName')
    start_date = Field('startDate')
    status = Field('status')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')

api.register(BackgroundJob)


class Baseline(Object):
    code = 'BLIN'
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_start_date = Field('actualStartDate')
    actual_work_required = Field('actualWorkRequired')
    auto_generated = Field('autoGenerated')
    budget = Field('budget')
    condition = Field('condition')
    cpi = Field('cpi')
    csi = Field('csi')
    customer_id = Field('customerID')
    duration_minutes = Field('durationMinutes')
    eac = Field('eac')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    is_default = Field('isDefault')
    name = Field('name')
    percent_complete = Field('percentComplete')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_start_date = Field('plannedStartDate')
    progress_status = Field('progressStatus')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_start_date = Field('projectedStartDate')
    spi = Field('spi')
    work_required = Field('workRequired')
    customer = Reference('customer')
    project = Reference('project')
    baseline_tasks = Collection('baselineTasks')

api.register(Baseline)


class BaselineTask(Object):
    code = 'BSTSK'
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_start_date = Field('actualStartDate')
    actual_work_required = Field('actualWorkRequired')
    baseline_id = Field('baselineID')
    cpi = Field('cpi')
    csi = Field('csi')
    customer_id = Field('customerID')
    duration_minutes = Field('durationMinutes')
    duration_unit = Field('durationUnit')
    eac = Field('eac')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    is_default = Field('isDefault')
    name = Field('name')
    percent_complete = Field('percentComplete')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_start_date = Field('plannedStartDate')
    progress_status = Field('progressStatus')
    projected_completion_date = Field('projectedCompletionDate')
    projected_start_date = Field('projectedStartDate')
    spi = Field('spi')
    task_id = Field('taskID')
    work_required = Field('workRequired')
    baseline = Reference('baseline')
    customer = Reference('customer')
    task = Reference('task')

api.register(BaselineTask)


class BillingRecord(Object):
    code = 'BILL'
    amount = Field('amount')
    billing_date = Field('billingDate')
    customer_id = Field('customerID')
    description = Field('description')
    display_name = Field('displayName')
    ext_ref_id = Field('extRefID')
    invoice_id = Field('invoiceID')
    other_amount = Field('otherAmount')
    po_number = Field('poNumber')
    project_id = Field('projectID')
    status = Field('status')
    customer = Reference('customer')
    project = Reference('project')
    billable_tasks = Collection('billableTasks')
    expenses = Collection('expenses')
    hours = Collection('hours')

api.register(BillingRecord)


class Category(Object):
    code = 'CTGY'
    cat_obj_code = Field('catObjCode')
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    ext_ref_id = Field('extRefID')
    group_id = Field('groupID')
    has_calculated_fields = Field('hasCalculatedFields')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    group = Reference('group')
    last_updated_by = Reference('lastUpdatedBy')
    category_parameters = Collection('categoryParameters')
    other_groups = Collection('otherGroups')

api.register(Category)


class CategoryParameter(Object):
    code = 'CTGYPA'
    category_id = Field('categoryID')
    custom_expression = Field('customExpression')
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    is_invalid_expression = Field('isInvalidExpression')
    is_required = Field('isRequired')
    parameter_group_id = Field('parameterGroupID')
    parameter_id = Field('parameterID')
    row_shared = Field('rowShared')
    security_level = Field('securityLevel')
    view_security_level = Field('viewSecurityLevel')
    category = Reference('category')
    category_parameter_expression = Reference('categoryParameterExpression')
    customer = Reference('customer')
    parameter = Reference('parameter')
    parameter_group = Reference('parameterGroup')

api.register(CategoryParameter)


class CategoryParameterExpression(Object):
    code = 'CTGPEX'
    custom_expression = Field('customExpression')
    customer_id = Field('customerID')
    has_finance_fields = Field('hasFinanceFields')
    category_parameter = Reference('categoryParameter')
    customer = Reference('customer')

api.register(CategoryParameterExpression)


class Company(Object):
    code = 'CMPY'
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_rate_override = Field('hasRateOverride')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    rates = Collection('rates')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

api.register(Company)


class CustomEnum(Object):
    code = 'CSTEM'
    color = Field('color')
    customer_id = Field('customerID')
    description = Field('description')
    enum_class = Field('enumClass')
    equates_with = Field('equatesWith')
    ext_ref_id = Field('extRefID')
    is_primary = Field('isPrimary')
    label = Field('label')
    value = Field('value')
    value_as_int = Field('valueAsInt')
    value_as_string = Field('valueAsString')
    customer = Reference('customer')

    def get_default_op_task_priority_enum(self):
        """
        The ``getDefaultOpTaskPriorityEnum`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultOpTaskPriorityEnum', params)
        return data['result']

    def get_default_project_status_enum(self):
        """
        The ``getDefaultProjectStatusEnum`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultProjectStatusEnum', params)
        return data['result']

    def get_default_severity_enum(self):
        """
        The ``getDefaultSeverityEnum`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultSeverityEnum', params)
        return data['result']

    def get_default_task_priority_enum(self):
        """
        The ``getDefaultTaskPriorityEnum`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultTaskPriorityEnum', params)
        return data['result']

api.register(CustomEnum)


class Customer(Object):
    code = 'CUST'
    account_rep_id = Field('accountRepID')
    address = Field('address')
    address2 = Field('address2')
    admin_acct_name = Field('adminAcctName')
    admin_acct_password = Field('adminAcctPassword')
    api_concurrency_limit = Field('apiConcurrencyLimit')
    biz_rule_exclusions = Field('bizRuleExclusions')
    city = Field('city')
    cloneable = Field('cloneable')
    country = Field('country')
    currency = Field('currency')
    custom_enum_types = Field('customEnumTypes')
    customer_config_map_id = Field('customerConfigMapID')
    customer_urlconfig_map_id = Field('customerURLConfigMapID')
    dd_svnversion = Field('ddSVNVersion')
    demo_baseline_date = Field('demoBaselineDate')
    description = Field('description')
    disabled_date = Field('disabledDate')
    document_size = Field('documentSize')
    domain = Field('domain')
    email_addr = Field('emailAddr')
    entry_date = Field('entryDate')
    eval_exp_date = Field('evalExpDate')
    exp_date = Field('expDate')
    ext_ref_id = Field('extRefID')
    external_document_storage = Field('externalDocumentStorage')
    external_users_enabled = Field('externalUsersEnabled')
    extra_document_storage = Field('extraDocumentStorage')
    firstname = Field('firstname')
    full_users = Field('fullUsers')
    golden = Field('golden')
    has_documents = Field('hasDocuments')
    has_preview_access = Field('hasPreviewAccess')
    has_timed_notifications = Field('hasTimedNotifications')
    help_desk_config_map_id = Field('helpDeskConfigMapID')
    inline_java_script_config_map_id = Field('inlineJavaScriptConfigMapID')
    is_apienabled = Field('isAPIEnabled')
    is_disabled = Field('isDisabled')
    is_enterprise = Field('isEnterprise')
    is_marketing_solutions_enabled = Field('isMarketingSolutionsEnabled')
    is_migrated_to_anaconda = Field('isMigratedToAnaconda')
    is_portal_profile_migrated = Field('isPortalProfileMigrated')
    is_soapenabled = Field('isSOAPEnabled')
    is_warning_disabled = Field('isWarningDisabled')
    journal_field_limit = Field('journalFieldLimit')
    last_remind_date = Field('lastRemindDate')
    last_usage_report_date = Field('lastUsageReportDate')
    lastname = Field('lastname')
    limited_users = Field('limitedUsers')
    locale = Field('locale')
    name = Field('name')
    need_license_agreement = Field('needLicenseAgreement')
    next_usage_report_date = Field('nextUsageReportDate')
    notification_config_map_id = Field('notificationConfigMapID')
    on_demand_options = Field('onDemandOptions')
    op_task_count_limit = Field('opTaskCountLimit')
    overdraft_exp_date = Field('overdraftExpDate')
    password_config_map_id = Field('passwordConfigMapID')
    phone_number = Field('phoneNumber')
    portfolio_management_config_map_id = Field('portfolioManagementConfigMapID')
    postal_code = Field('postalCode')
    project_management_config_map_id = Field('projectManagementConfigMapID')
    proof_account_id = Field('proofAccountID')
    record_limit = Field('recordLimit')
    requestor_users = Field('requestorUsers')
    reseller_id = Field('resellerID')
    review_users = Field('reviewUsers')
    sandbox_count = Field('sandboxCount')
    sandbox_refreshing = Field('sandboxRefreshing')
    security_model_type = Field('securityModelType')
    sso_type = Field('ssoType')
    state = Field('state')
    status = Field('status')
    style_sheet = Field('styleSheet')
    task_count_limit = Field('taskCountLimit')
    team_users = Field('teamUsers')
    time_zone = Field('timeZone')
    timesheet_config_map_id = Field('timesheetConfigMapID')
    trial = Field('trial')
    ui_config_map_id = Field('uiConfigMapID')
    usage_report_attempts = Field('usageReportAttempts')
    use_external_document_storage = Field('useExternalDocumentStorage')
    user_invite_config_map_id = Field('userInviteConfigMapID')
    welcome_email_addresses = Field('welcomeEmailAddresses')
    approval_processes = Collection('approvalProcesses')
    categories = Collection('categories')
    custom_enums = Collection('customEnums')
    documents = Collection('documents')
    expense_types = Collection('expenseTypes')
    groups = Collection('groups')
    hour_types = Collection('hourTypes')
    layout_templates = Collection('layoutTemplates')
    milestone_paths = Collection('milestonePaths')
    parameter_groups = Collection('parameterGroups')
    parameters = Collection('parameters')
    resource_pools = Collection('resourcePools')
    risk_types = Collection('riskTypes')
    roles = Collection('roles')
    schedules = Collection('schedules')
    score_cards = Collection('scoreCards')
    ui_filters = Collection('uiFilters')
    ui_group_bys = Collection('uiGroupBys')
    ui_views = Collection('uiViews')

api.register(Customer)


class CustomerPreferences(Object):
    code = 'CUSTPR'
    name = Field('name')
    obj_code = Field('objCode')
    possible_values = Field('possibleValues')
    value = Field('value')

api.register(CustomerPreferences)


class Document(Object):
    code = 'DOCU'
    category_id = Field('categoryID')
    checked_out_by_id = Field('checkedOutByID')
    current_version_id = Field('currentVersionID')
    customer_id = Field('customerID')
    description = Field('description')
    doc_obj_code = Field('docObjCode')
    document_request_id = Field('documentRequestID')
    download_url = Field('downloadURL')
    ext_ref_id = Field('extRefID')
    external_integration_type = Field('externalIntegrationType')
    handle = Field('handle')
    has_notes = Field('hasNotes')
    is_dir = Field('isDir')
    is_private = Field('isPrivate')
    is_public = Field('isPublic')
    iteration_id = Field('iterationID')
    last_mod_date = Field('lastModDate')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    master_task_id = Field('masterTaskID')
    name = Field('name')
    obj_id = Field('objID')
    op_task_id = Field('opTaskID')
    owner_id = Field('ownerID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    public_token = Field('publicToken')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    reference_object_name = Field('referenceObjectName')
    release_version_id = Field('releaseVersionID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    top_doc_obj_code = Field('topDocObjCode')
    top_obj_id = Field('topObjID')
    user_id = Field('userID')
    category = Reference('category')
    checked_out_by = Reference('checkedOutBy')
    current_version = Reference('currentVersion')
    customer = Reference('customer')
    iteration = Reference('iteration')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    op_task = Reference('opTask')
    owner = Reference('owner')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    release_version = Reference('releaseVersion')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    user = Reference('user')
    access_rules = Collection('accessRules')
    approvals = Collection('approvals')
    folders = Collection('folders')
    groups = Collection('groups')
    subscribers = Collection('subscribers')
    versions = Collection('versions')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def move(self, obj_id=None, doc_obj_code=None):
        """
        The ``move`` action.
        
        :param obj_id: objID (type: ``string``)
        :param doc_obj_code: docObjCode (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if doc_obj_code is not None: params['docObjCode'] = doc_obj_code
        data = self.session.put(self.api_url()+'/move', params)
        

api.register(Document)


class DocumentApproval(Object):
    code = 'DOCAPL'
    approval_date = Field('approvalDate')
    approver_id = Field('approverID')
    auto_document_share_id = Field('autoDocumentShareID')
    customer_id = Field('customerID')
    document_id = Field('documentID')
    note_id = Field('noteID')
    request_date = Field('requestDate')
    requestor_id = Field('requestorID')
    status = Field('status')
    approver = Reference('approver')
    customer = Reference('customer')
    document = Reference('document')
    note = Reference('note')
    requestor = Reference('requestor')

api.register(DocumentApproval)


class DocumentFolder(Object):
    code = 'DOCFDR'
    customer_id = Field('customerID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    issue_id = Field('issueID')
    iteration_id = Field('iterationID')
    name = Field('name')
    parent_id = Field('parentID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    user_id = Field('userID')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    issue = Reference('issue')
    iteration = Reference('iteration')
    parent = Reference('parent')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    user = Reference('user')
    children = Collection('children')
    documents = Collection('documents')

api.register(DocumentFolder)


class DocumentVersion(Object):
    code = 'DOCV'
    customer_id = Field('customerID')
    doc_size = Field('docSize')
    document_id = Field('documentID')
    document_type_label = Field('documentTypeLabel')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext = Field('ext')
    external_download_url = Field('externalDownloadURL')
    external_integration_type = Field('externalIntegrationType')
    external_preview_url = Field('externalPreviewURL')
    external_save_location = Field('externalSaveLocation')
    external_storage_id = Field('externalStorageID')
    file_name = Field('fileName')
    format_doc_size = Field('formatDocSize')
    format_entry_date = Field('formatEntryDate')
    handle = Field('handle')
    is_proofable = Field('isProofable')
    proof_id = Field('proofID')
    proof_status = Field('proofStatus')
    version = Field('version')
    customer = Reference('customer')
    document = Reference('document')
    entered_by = Reference('enteredBy')

api.register(DocumentVersion)


class ExchangeRate(Object):
    code = 'EXRATE'
    currency = Field('currency')
    customer_id = Field('customerID')
    ext_ref_id = Field('extRefID')
    project_id = Field('projectID')
    rate = Field('rate')
    template_id = Field('templateID')
    customer = Reference('customer')
    project = Reference('project')
    template = Reference('template')

api.register(ExchangeRate)


class Expense(Object):
    code = 'EXPNS'
    actual_amount = Field('actualAmount')
    actual_unit_amount = Field('actualUnitAmount')
    billing_record_id = Field('billingRecordID')
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    description = Field('description')
    effective_date = Field('effectiveDate')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    exp_obj_code = Field('expObjCode')
    expense_type_id = Field('expenseTypeID')
    ext_ref_id = Field('extRefID')
    is_billable = Field('isBillable')
    is_reimbursable = Field('isReimbursable')
    is_reimbursed = Field('isReimbursed')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    master_task_id = Field('masterTaskID')
    obj_id = Field('objID')
    planned_amount = Field('plannedAmount')
    planned_date = Field('plannedDate')
    planned_unit_amount = Field('plannedUnitAmount')
    project_id = Field('projectID')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    reference_object_name = Field('referenceObjectName')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    top_obj_code = Field('topObjCode')
    top_obj_id = Field('topObjID')
    top_reference_obj_code = Field('topReferenceObjCode')
    top_reference_obj_id = Field('topReferenceObjID')
    billing_record = Reference('billingRecord')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    expense_type = Reference('expenseType')
    last_updated_by = Reference('lastUpdatedBy')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def move(self, obj_id=None, exp_obj_code=None):
        """
        The ``move`` action.
        
        :param obj_id: objID (type: ``string``)
        :param exp_obj_code: expObjCode (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if exp_obj_code is not None: params['expObjCode'] = exp_obj_code
        data = self.session.put(self.api_url()+'/move', params)
        

api.register(Expense)


class ExpenseType(Object):
    code = 'EXPTYP'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    display_per = Field('displayPer')
    display_rate_unit = Field('displayRateUnit')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    rate = Field('rate')
    rate_unit = Field('rateUnit')
    customer = Reference('customer')

api.register(ExpenseType)


class Favorite(Object):
    code = 'FVRITE'
    customer_id = Field('customerID')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    user_id = Field('userID')
    customer = Reference('customer')
    user = Reference('user')

api.register(Favorite)


class FinancialData(Object):
    code = 'FINDAT'
    actual_expense_cost = Field('actualExpenseCost')
    actual_fixed_revenue = Field('actualFixedRevenue')
    actual_labor_cost = Field('actualLaborCost')
    actual_labor_cost_hours = Field('actualLaborCostHours')
    actual_labor_revenue = Field('actualLaborRevenue')
    allocationdate = Field('allocationdate')
    customer_id = Field('customerID')
    fixed_cost = Field('fixedCost')
    is_split = Field('isSplit')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_fixed_revenue = Field('plannedFixedRevenue')
    planned_labor_cost = Field('plannedLaborCost')
    planned_labor_cost_hours = Field('plannedLaborCostHours')
    planned_labor_revenue = Field('plannedLaborRevenue')
    project_id = Field('projectID')
    total_actual_cost = Field('totalActualCost')
    total_actual_revenue = Field('totalActualRevenue')
    total_planned_cost = Field('totalPlannedCost')
    total_planned_revenue = Field('totalPlannedRevenue')
    total_variance_cost = Field('totalVarianceCost')
    total_variance_revenue = Field('totalVarianceRevenue')
    variance_expense_cost = Field('varianceExpenseCost')
    variance_labor_cost = Field('varianceLaborCost')
    variance_labor_cost_hours = Field('varianceLaborCostHours')
    variance_labor_revenue = Field('varianceLaborRevenue')
    customer = Reference('customer')
    project = Reference('project')

api.register(FinancialData)


class Group(Object):
    code = 'GROUP'
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')

api.register(Group)


class Hour(Object):
    code = 'HOUR'
    actual_cost = Field('actualCost')
    approved_by_id = Field('approvedByID')
    approved_on_date = Field('approvedOnDate')
    billing_record_id = Field('billingRecordID')
    customer_id = Field('customerID')
    description = Field('description')
    dup_id = Field('dupID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_rate_override = Field('hasRateOverride')
    hour_type_id = Field('hourTypeID')
    hours = Field('hours')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    op_task_id = Field('opTaskID')
    owner_id = Field('ownerID')
    project_id = Field('projectID')
    project_overhead_id = Field('projectOverheadID')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    resource_revenue = Field('resourceRevenue')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    status = Field('status')
    task_id = Field('taskID')
    timesheet_id = Field('timesheetID')
    approved_by = Reference('approvedBy')
    billing_record = Reference('billingRecord')
    customer = Reference('customer')
    hour_type = Reference('hourType')
    last_updated_by = Reference('lastUpdatedBy')
    op_task = Reference('opTask')
    owner = Reference('owner')
    project = Reference('project')
    project_overhead = Reference('projectOverhead')
    role = Reference('role')
    task = Reference('task')
    timesheet = Reference('timesheet')

api.register(Hour)


class HourType(Object):
    code = 'HOURT'
    app_global_id = Field('appGlobalID')
    count_as_revenue = Field('countAsRevenue')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    display_obj_obj_code = Field('displayObjObjCode')
    ext_ref_id = Field('extRefID')
    is_active = Field('isActive')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    overhead_type = Field('overheadType')
    scope = Field('scope')
    customer = Reference('customer')
    users = Collection('users')

api.register(HourType)


class Issue(Object):
    code = 'OPTASK'
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_start_date = Field('actualStartDate')
    actual_work_required = Field('actualWorkRequired')
    actual_work_required_expression = Field('actualWorkRequiredExpression')
    age_range_as_string = Field('ageRangeAsString')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    assigned_to_id = Field('assignedToID')
    audit_types = Field('auditTypes')
    auto_closure_date = Field('autoClosureDate')
    can_start = Field('canStart')
    category_id = Field('categoryID')
    commit_date = Field('commitDate')
    commit_date_range = Field('commitDateRange')
    condition = Field('condition')
    current_approval_step_id = Field('currentApprovalStepID')
    current_status_duration = Field('currentStatusDuration')
    customer_id = Field('customerID')
    description = Field('description')
    due_date = Field('dueDate')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    first_response = Field('firstResponse')
    has_documents = Field('hasDocuments')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_resolvables = Field('hasResolvables')
    has_timed_notifications = Field('hasTimedNotifications')
    how_old = Field('howOld')
    is_complete = Field('isComplete')
    is_help_desk = Field('isHelpDesk')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    number_of_children = Field('numberOfChildren')
    op_task_type = Field('opTaskType')
    op_task_type_label = Field('opTaskTypeLabel')
    owner_id = Field('ownerID')
    planned_completion_date = Field('plannedCompletionDate')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_start_date = Field('plannedStartDate')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    project_id = Field('projectID')
    projected_duration_minutes = Field('projectedDurationMinutes')
    projected_start_date = Field('projectedStartDate')
    queue_topic_id = Field('queueTopicID')
    reference_number = Field('referenceNumber')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_duration_minutes = Field('remainingDurationMinutes')
    resolution_time = Field('resolutionTime')
    resolve_op_task_id = Field('resolveOpTaskID')
    resolve_project_id = Field('resolveProjectID')
    resolve_task_id = Field('resolveTaskID')
    resolving_obj_code = Field('resolvingObjCode')
    resolving_obj_id = Field('resolvingObjID')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    severity = Field('severity')
    source_obj_code = Field('sourceObjCode')
    source_obj_id = Field('sourceObjID')
    source_task_id = Field('sourceTaskID')
    status = Field('status')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    team_id = Field('teamID')
    url = Field('url')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    category = Reference('category')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    owner = Reference('owner')
    parent = Reference('parent')
    primary_assignment = Reference('primaryAssignment')
    project = Reference('project')
    queue_topic = Reference('queueTopic')
    rejection_issue = Reference('rejectionIssue')
    resolve_op_task = Reference('resolveOpTask')
    resolve_project = Reference('resolveProject')
    resolve_task = Reference('resolveTask')
    role = Reference('role')
    source_task = Reference('sourceTask')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    work_item = Reference('workItem')
    access_rules = Collection('accessRules')
    all_priorities = Collection('allPriorities')
    all_severities = Collection('allSeverities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    assignments = Collection('assignments')
    documents = Collection('documents')
    done_statuses = Collection('doneStatuses')
    hours = Collection('hours')
    resolvables = Collection('resolvables')
    updates = Collection('updates')

    def accept_work(self):
        """
        The ``acceptWork`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/acceptWork', params)
        

    def approve_approval(self, user_id=None, username=None, password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``approveApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/approveApproval', params)
        

    def assign(self, obj_id=None, obj_code=None):
        """
        The ``assign`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        data = self.session.put(self.api_url()+'/assign', params)
        

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def mark_done(self, status=None):
        """
        The ``markDone`` action.
        
        :param status: status (type: ``string``)
        """
        params = {}
        if status is not None: params['status'] = status
        data = self.session.put(self.api_url()+'/markDone', params)
        

    def mark_not_done(self, assignment_id=None):
        """
        The ``markNotDone`` action.
        
        :param assignment_id: assignmentID (type: ``string``)
        """
        params = {}
        if assignment_id is not None: params['assignmentID'] = assignment_id
        data = self.session.put(self.api_url()+'/markNotDone', params)
        

    def move(self, project_id=None):
        """
        The ``move`` action.
        
        :param project_id: projectID (type: ``string``)
        """
        params = {}
        if project_id is not None: params['projectID'] = project_id
        data = self.session.put(self.api_url()+'/move', params)
        

    def move_to_task(self, project_id=None, parent_id=None):
        """
        The ``moveToTask`` action.
        
        :param project_id: projectID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        """
        params = {}
        if project_id is not None: params['projectID'] = project_id
        if parent_id is not None: params['parentID'] = parent_id
        data = self.session.put(self.api_url()+'/moveToTask', params)
        

    def recall_approval(self):
        """
        The ``recallApproval`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/recallApproval', params)
        

    def reject_approval(self, user_id=None, username=None, password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``rejectApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/rejectApproval', params)
        

    def reply_to_assignment(self, note_text=None, commit_date=None):
        """
        The ``replyToAssignment`` action.
        
        :param note_text: noteText (type: ``string``)
        :param commit_date: commitDate (type: ``dateTime``)
        """
        params = {}
        if note_text is not None: params['noteText'] = note_text
        if commit_date is not None: params['commitDate'] = commit_date
        data = self.session.put(self.api_url()+'/replyToAssignment', params)
        

    def unaccept_work(self):
        """
        The ``unacceptWork`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unacceptWork', params)
        

    def unassign(self, user_id=None):
        """
        The ``unassign`` action.
        
        :param user_id: userID (type: ``string``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/unassign', params)
        

    def add_comment(self, text):
        """
        Add a comment to the current object containing the supplied text.

        The new :class:`Comment` instance is returned, it does not need to be
        saved.
        """

        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.code,
            obj_id = self.id
        )
        comment.save()
        return comment

    def convert_to_task(self):
        """
        Convert this issue to a task.
        The newly converted task will be returned, it does not need to be
        saved.
        """
        data = self.session.put(
            self.api_url()+'/convertToTask',
            params=dict(
                updates=dict(
                    options=['preserveIssue',
                             'preservePrimaryContact',
                             'preserveUpdates'],
                    task=dict(name=self.name,
                              description=self.description,
                              enteredByID=self.entered_by_id,
                              )
            )))
        return self.session.api.Task(self.session, ID=data['result'])

api.register(Issue)


class Iteration(Object):
    code = 'ITRN'
    url = Field('URL')
    capacity = Field('capacity')
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    end_date = Field('endDate')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    estimate_completed = Field('estimateCompleted')
    focus_factor = Field('focusFactor')
    goal = Field('goal')
    has_documents = Field('hasDocuments')
    has_notes = Field('hasNotes')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    owner_id = Field('ownerID')
    percent_complete = Field('percentComplete')
    start_date = Field('startDate')
    status = Field('status')
    target_percent_complete = Field('targetPercentComplete')
    task_ids = Field('taskIDs')
    team_id = Field('teamID')
    total_estimate = Field('totalEstimate')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    owner = Reference('owner')
    team = Reference('team')
    documents = Collection('documents')

api.register(Iteration)


class JournalEntry(Object):
    code = 'JRNLE'
    assignment_id = Field('assignmentID')
    aux1 = Field('aux1')
    aux2 = Field('aux2')
    aux3 = Field('aux3')
    billing_record_id = Field('billingRecordID')
    change_type = Field('changeType')
    customer_id = Field('customerID')
    document_approval_id = Field('documentApprovalID')
    document_id = Field('documentID')
    document_share_id = Field('documentShareID')
    duration_minutes = Field('durationMinutes')
    edited_by_id = Field('editedByID')
    entry_date = Field('entryDate')
    expense_id = Field('expenseID')
    ext_ref_id = Field('extRefID')
    field_name = Field('fieldName')
    flags = Field('flags')
    hour_id = Field('hourID')
    new_date_val = Field('newDateVal')
    new_number_val = Field('newNumberVal')
    new_text_val = Field('newTextVal')
    num_likes = Field('numLikes')
    num_replies = Field('numReplies')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    old_date_val = Field('oldDateVal')
    old_number_val = Field('oldNumberVal')
    old_text_val = Field('oldTextVal')
    op_task_id = Field('opTaskID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    sub_obj_code = Field('subObjCode')
    sub_obj_id = Field('subObjID')
    task_id = Field('taskID')
    template_id = Field('templateID')
    timesheet_id = Field('timesheetID')
    top_obj_code = Field('topObjCode')
    top_obj_id = Field('topObjID')
    user_id = Field('userID')
    assignment = Reference('assignment')
    billing_record = Reference('billingRecord')
    customer = Reference('customer')
    document = Reference('document')
    document_approval = Reference('documentApproval')
    edited_by = Reference('editedBy')
    expense = Reference('expense')
    hour = Reference('hour')
    op_task = Reference('opTask')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    timesheet = Reference('timesheet')
    user = Reference('user')
    replies = Collection('replies')

    def like(self):
        """
        The ``like`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/like', params)
        

    def unlike(self):
        """
        The ``unlike`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unlike', params)
        

api.register(JournalEntry)


class LayoutTemplate(Object):
    code = 'LYTMPL'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    default_nav_item = Field('defaultNavItem')
    description = Field('description')
    description_key = Field('descriptionKey')
    ext_ref_id = Field('extRefID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    license_type = Field('licenseType')
    name = Field('name')
    name_key = Field('nameKey')
    nav_bar = Field('navBar')
    nav_items = Field('navItems')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    customer = Reference('customer')
    last_updated_by = Reference('lastUpdatedBy')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')
    ui_filters = Collection('uiFilters')
    ui_group_bys = Collection('uiGroupBys')
    ui_views = Collection('uiViews')

api.register(LayoutTemplate)


class MessageArg(Object):
    code = 'MSGARG'
    allowed_actions = Field('allowedActions')
    color = Field('color')
    href = Field('href')
    objcode = Field('objcode')
    objid = Field('objid')
    text = Field('text')
    type = Field('type')

api.register(MessageArg)


class Milestone(Object):
    code = 'MILE'
    color = Field('color')
    customer_id = Field('customerID')
    description = Field('description')
    ext_ref_id = Field('extRefID')
    milestone_path_id = Field('milestonePathID')
    name = Field('name')
    sequence = Field('sequence')
    customer = Reference('customer')
    milestone_path = Reference('milestonePath')

api.register(Milestone)


class MilestonePath(Object):
    code = 'MPATH'
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    groups = Collection('groups')
    milestones = Collection('milestones')

api.register(MilestonePath)


class NonWorkDay(Object):
    code = 'NONWKD'
    customer_id = Field('customerID')
    non_work_date = Field('nonWorkDate')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    schedule_day = Field('scheduleDay')
    schedule_id = Field('scheduleID')
    user_id = Field('userID')
    customer = Reference('customer')
    schedule = Reference('schedule')
    user = Reference('user')

api.register(NonWorkDay)


class Note(Object):
    code = 'NOTE'
    attach_document_id = Field('attachDocumentID')
    attach_obj_code = Field('attachObjCode')
    attach_obj_id = Field('attachObjID')
    attach_op_task_id = Field('attachOpTaskID')
    audit_text = Field('auditText')
    audit_type = Field('auditType')
    customer_id = Field('customerID')
    document_id = Field('documentID')
    email_users = Field('emailUsers')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    format_entry_date = Field('formatEntryDate')
    has_replies = Field('hasReplies')
    indent = Field('indent')
    is_deleted = Field('isDeleted')
    is_message = Field('isMessage')
    is_private = Field('isPrivate')
    is_reply = Field('isReply')
    iteration_id = Field('iterationID')
    note_obj_code = Field('noteObjCode')
    note_text = Field('noteText')
    num_likes = Field('numLikes')
    num_replies = Field('numReplies')
    obj_id = Field('objID')
    op_task_id = Field('opTaskID')
    owner_id = Field('ownerID')
    parent_endorsement_id = Field('parentEndorsementID')
    parent_journal_entry_id = Field('parentJournalEntryID')
    parent_note_id = Field('parentNoteID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    reference_object_name = Field('referenceObjectName')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    subject = Field('subject')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    thread_date = Field('threadDate')
    thread_id = Field('threadID')
    timesheet_id = Field('timesheetID')
    top_note_obj_code = Field('topNoteObjCode')
    top_obj_id = Field('topObjID')
    top_reference_object_name = Field('topReferenceObjectName')
    user_id = Field('userID')
    attach_document = Reference('attachDocument')
    attach_op_task = Reference('attachOpTask')
    customer = Reference('customer')
    document = Reference('document')
    iteration = Reference('iteration')
    op_task = Reference('opTask')
    owner = Reference('owner')
    parent_journal_entry = Reference('parentJournalEntry')
    parent_note = Reference('parentNote')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    timesheet = Reference('timesheet')
    user = Reference('user')
    replies = Collection('replies')
    tags = Collection('tags')

    def like(self):
        """
        The ``like`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/like', params)
        

    def unlike(self):
        """
        The ``unlike`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unlike', params)
        

    def add_comment(self, text):
        """
        Add a comment to this comment.

        The new :class:`Comment` instance is returned, it does not need to be
        saved.
        """
        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.note_obj_code,
            obj_id = self.obj_id,
            parent_note_id=self.id
        )
        comment.save()
        return comment

api.register(Note)


class NoteTag(Object):
    code = 'NTAG'
    customer_id = Field('customerID')
    length = Field('length')
    note_id = Field('noteID')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    reference_object_name = Field('referenceObjectName')
    start_idx = Field('startIdx')
    team_id = Field('teamID')
    user_id = Field('userID')
    customer = Reference('customer')
    note = Reference('note')
    team = Reference('team')
    user = Reference('user')

api.register(NoteTag)


class Parameter(Object):
    code = 'PARAM'
    customer_id = Field('customerID')
    data_type = Field('dataType')
    description = Field('description')
    display_size = Field('displaySize')
    display_type = Field('displayType')
    ext_ref_id = Field('extRefID')
    format_constraint = Field('formatConstraint')
    is_required = Field('isRequired')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    customer = Reference('customer')
    last_updated_by = Reference('lastUpdatedBy')
    parameter_options = Collection('parameterOptions')

api.register(Parameter)


class ParameterGroup(Object):
    code = 'PGRP'
    customer_id = Field('customerID')
    description = Field('description')
    display_order = Field('displayOrder')
    ext_ref_id = Field('extRefID')
    is_default = Field('isDefault')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    customer = Reference('customer')
    last_updated_by = Reference('lastUpdatedBy')

api.register(ParameterGroup)


class ParameterOption(Object):
    code = 'POPT'
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    ext_ref_id = Field('extRefID')
    is_default = Field('isDefault')
    is_hidden = Field('isHidden')
    label = Field('label')
    parameter_id = Field('parameterID')
    value = Field('value')
    customer = Reference('customer')
    parameter = Reference('parameter')

api.register(ParameterOption)


class Portfolio(Object):
    code = 'PORT'
    aligned = Field('aligned')
    alignment_score_card_id = Field('alignmentScoreCardID')
    audit_types = Field('auditTypes')
    budget = Field('budget')
    category_id = Field('categoryID')
    currency = Field('currency')
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_documents = Field('hasDocuments')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    is_active = Field('isActive')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    net_value = Field('netValue')
    on_budget = Field('onBudget')
    on_time = Field('onTime')
    owner_id = Field('ownerID')
    roi = Field('roi')
    alignment_score_card = Reference('alignmentScoreCard')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    owner = Reference('owner')
    access_rules = Collection('accessRules')
    documents = Collection('documents')
    groups = Collection('groups')
    programs = Collection('programs')
    projects = Collection('projects')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

api.register(Portfolio)


class Predecessor(Object):
    code = 'PRED'
    customer_id = Field('customerID')
    is_cp = Field('isCP')
    is_enforced = Field('isEnforced')
    lag_days = Field('lagDays')
    lag_type = Field('lagType')
    predecessor_id = Field('predecessorID')
    predecessor_type = Field('predecessorType')
    successor_id = Field('successorID')
    customer = Reference('customer')
    predecessor = Reference('predecessor')
    successor = Reference('successor')

api.register(Predecessor)


class Program(Object):
    code = 'PRGM'
    audit_types = Field('auditTypes')
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_documents = Field('hasDocuments')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    owner_id = Field('ownerID')
    portfolio_id = Field('portfolioID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    owner = Reference('owner')
    portfolio = Reference('portfolio')
    access_rules = Collection('accessRules')
    documents = Collection('documents')
    projects = Collection('projects')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def move(self, portfolio_id=None, options=None):
        """
        The ``move`` action.
        
        :param portfolio_id: portfolioID (type: ``string``)
        :param options: options (type: ``string[]``)
        """
        params = {}
        if portfolio_id is not None: params['portfolioID'] = portfolio_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/move', params)
        

api.register(Program)


class Project(Object):
    code = 'PROJ'
    bccompletion_state = Field('BCCompletionState')
    url = Field('URL')
    actual_benefit = Field('actualBenefit')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration_expression = Field('actualDurationExpression')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_expense_cost = Field('actualExpenseCost')
    actual_hours_last_month = Field('actualHoursLastMonth')
    actual_hours_last_three_months = Field('actualHoursLastThreeMonths')
    actual_hours_this_month = Field('actualHoursThisMonth')
    actual_hours_two_months_ago = Field('actualHoursTwoMonthsAgo')
    actual_labor_cost = Field('actualLaborCost')
    actual_revenue = Field('actualRevenue')
    actual_risk_cost = Field('actualRiskCost')
    actual_start_date = Field('actualStartDate')
    actual_value = Field('actualValue')
    actual_work_required = Field('actualWorkRequired')
    actual_work_required_expression = Field('actualWorkRequiredExpression')
    alignment = Field('alignment')
    alignment_score_card_id = Field('alignmentScoreCardID')
    all_approved_hours = Field('allApprovedHours')
    all_unapproved_hours = Field('allUnapprovedHours')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    audit_types = Field('auditTypes')
    auto_baseline_recur_on = Field('autoBaselineRecurOn')
    auto_baseline_recurrence_type = Field('autoBaselineRecurrenceType')
    billed_revenue = Field('billedRevenue')
    budget = Field('budget')
    budget_status = Field('budgetStatus')
    budgeted_completion_date = Field('budgetedCompletionDate')
    budgeted_cost = Field('budgetedCost')
    budgeted_hours = Field('budgetedHours')
    budgeted_labor_cost = Field('budgetedLaborCost')
    budgeted_start_date = Field('budgetedStartDate')
    business_case_status_label = Field('businessCaseStatusLabel')
    category_id = Field('categoryID')
    company_id = Field('companyID')
    completion_type = Field('completionType')
    condition = Field('condition')
    condition_type = Field('conditionType')
    converted_op_task_entry_date = Field('convertedOpTaskEntryDate')
    converted_op_task_name = Field('convertedOpTaskName')
    converted_op_task_originator_id = Field('convertedOpTaskOriginatorID')
    cpi = Field('cpi')
    csi = Field('csi')
    currency = Field('currency')
    current_approval_step_id = Field('currentApprovalStepID')
    customer_id = Field('customerID')
    deliverable_score_card_id = Field('deliverableScoreCardID')
    deliverable_success_score = Field('deliverableSuccessScore')
    deliverable_success_score_ratio = Field('deliverableSuccessScoreRatio')
    description = Field('description')
    display_order = Field('displayOrder')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    eac = Field('eac')
    enable_auto_baselines = Field('enableAutoBaselines')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    ext_ref_id = Field('extRefID')
    filter_hour_types = Field('filterHourTypes')
    finance_last_update_date = Field('financeLastUpdateDate')
    fixed_cost = Field('fixedCost')
    fixed_end_date = Field('fixedEndDate')
    fixed_revenue = Field('fixedRevenue')
    fixed_start_date = Field('fixedStartDate')
    group_id = Field('groupID')
    has_budget_conflict = Field('hasBudgetConflict')
    has_calc_error = Field('hasCalcError')
    has_completion_constraint = Field('hasCompletionConstraint')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_rate_override = Field('hasRateOverride')
    has_resolvables = Field('hasResolvables')
    has_start_constraint = Field('hasStartConstraint')
    has_timed_notifications = Field('hasTimedNotifications')
    last_calc_date = Field('lastCalcDate')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_mode = Field('levelingMode')
    milestone_path_id = Field('milestonePathID')
    name = Field('name')
    next_auto_baseline_date = Field('nextAutoBaselineDate')
    number_open_op_tasks = Field('numberOpenOpTasks')
    olv = Field('olv')
    optimization_score = Field('optimizationScore')
    owner_id = Field('ownerID')
    owner_privileges = Field('ownerPrivileges')
    percent_complete = Field('percentComplete')
    performance_index_method = Field('performanceIndexMethod')
    personal = Field('personal')
    planned_benefit = Field('plannedBenefit')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_risk_cost = Field('plannedRiskCost')
    planned_start_date = Field('plannedStartDate')
    planned_value = Field('plannedValue')
    pop_account_id = Field('popAccountID')
    portfolio_id = Field('portfolioID')
    portfolio_priority = Field('portfolioPriority')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    program_id = Field('programID')
    progress_status = Field('progressStatus')
    projected_completion_date = Field('projectedCompletionDate')
    projected_start_date = Field('projectedStartDate')
    queue_def_id = Field('queueDefID')
    reference_number = Field('referenceNumber')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_cost = Field('remainingCost')
    remaining_revenue = Field('remainingRevenue')
    remaining_risk_cost = Field('remainingRiskCost')
    resource_pool_id = Field('resourcePoolID')
    risk = Field('risk')
    risk_performance_index = Field('riskPerformanceIndex')
    roi = Field('roi')
    schedule_id = Field('scheduleID')
    schedule_mode = Field('scheduleMode')
    selected_on_portfolio_optimizer = Field('selectedOnPortfolioOptimizer')
    spi = Field('spi')
    sponsor_id = Field('sponsorID')
    status = Field('status')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    summary_completion_type = Field('summaryCompletionType')
    template_id = Field('templateID')
    total_hours = Field('totalHours')
    total_op_task_count = Field('totalOpTaskCount')
    total_task_count = Field('totalTaskCount')
    update_type = Field('updateType')
    version = Field('version')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    alignment_score_card = Reference('alignmentScoreCard')
    approval_process = Reference('approvalProcess')
    category = Reference('category')
    company = Reference('company')
    converted_op_task_originator = Reference('convertedOpTaskOriginator')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    default_baseline = Reference('defaultBaseline')
    deliverable_score_card = Reference('deliverableScoreCard')
    entered_by = Reference('enteredBy')
    exchange_rate = Reference('exchangeRate')
    group = Reference('group')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone_path = Reference('milestonePath')
    owner = Reference('owner')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    queue_def = Reference('queueDef')
    rejection_issue = Reference('rejectionIssue')
    resource_pool = Reference('resourcePool')
    schedule = Reference('schedule')
    sponsor = Reference('sponsor')
    submitted_by = Reference('submittedBy')
    template = Reference('template')
    access_rules = Collection('accessRules')
    alignment_values = Collection('alignmentValues')
    all_hours = Collection('allHours')
    all_priorities = Collection('allPriorities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    baselines = Collection('baselines')
    billing_records = Collection('billingRecords')
    deliverable_values = Collection('deliverableValues')
    documents = Collection('documents')
    exchange_rates = Collection('exchangeRates')
    expenses = Collection('expenses')
    hour_types = Collection('hourTypes')
    hours = Collection('hours')
    open_op_tasks = Collection('openOpTasks')
    project_user_roles = Collection('projectUserRoles')
    project_users = Collection('projectUsers')
    rates = Collection('rates')
    resolvables = Collection('resolvables')
    resource_allocations = Collection('resourceAllocations')
    risks = Collection('risks')
    roles = Collection('roles')
    routing_rules = Collection('routingRules')
    tasks = Collection('tasks')
    updates = Collection('updates')

    def approve_approval(self, user_id=None, approval_username=None, approval_password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``approveApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param approval_username: approvalUsername (type: ``string``)
        :param approval_password: approvalPassword (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if approval_username is not None: params['approvalUsername'] = approval_username
        if approval_password is not None: params['approvalPassword'] = approval_password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/approveApproval', params)
        

    def attach_template(self, template_id=None, predecessor_task_id=None, parent_task_id=None, exclude_template_task_ids=None, options=None):
        """
        The ``attachTemplate`` action.
        
        :param template_id: templateID (type: ``string``)
        :param predecessor_task_id: predecessorTaskID (type: ``string``)
        :param parent_task_id: parentTaskID (type: ``string``)
        :param exclude_template_task_ids: excludeTemplateTaskIDs (type: ``string[]``)
        :param options: options (type: ``string[]``)
        :return: ``string``
        """
        params = {}
        if template_id is not None: params['templateID'] = template_id
        if predecessor_task_id is not None: params['predecessorTaskID'] = predecessor_task_id
        if parent_task_id is not None: params['parentTaskID'] = parent_task_id
        if exclude_template_task_ids is not None: params['excludeTemplateTaskIDs'] = exclude_template_task_ids
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/attachTemplate', params)
        return data['result']

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def calculate_finance(self):
        """
        The ``calculateFinance`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateFinance', params)
        

    def calculate_timeline(self):
        """
        The ``calculateTimeline`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateTimeline', params)
        

    def recall_approval(self):
        """
        The ``recallApproval`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/recallApproval', params)
        

    def reject_approval(self, user_id=None, approval_username=None, approval_password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``rejectApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param approval_username: approvalUsername (type: ``string``)
        :param approval_password: approvalPassword (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if approval_username is not None: params['approvalUsername'] = approval_username
        if approval_password is not None: params['approvalPassword'] = approval_password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/rejectApproval', params)
        

    def set_budget_to_schedule(self):
        """
        The ``setBudgetToSchedule`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/setBudgetToSchedule', params)
        

api.register(Project)


class ProjectUser(Object):
    code = 'PRTU'
    customer_id = Field('customerID')
    project_id = Field('projectID')
    user_id = Field('userID')
    customer = Reference('customer')
    project = Reference('project')
    user = Reference('user')

api.register(ProjectUser)


class ProjectUserRole(Object):
    code = 'PTEAM'
    customer_id = Field('customerID')
    project_id = Field('projectID')
    role_id = Field('roleID')
    user_id = Field('userID')
    customer = Reference('customer')
    project = Reference('project')
    role = Reference('role')
    user = Reference('user')

api.register(ProjectUserRole)


class QueueDef(Object):
    code = 'QUED'
    add_op_task_style = Field('addOpTaskStyle')
    allowed_op_task_types = Field('allowedOpTaskTypes')
    allowed_queue_topic_ids = Field('allowedQueueTopicIDs')
    customer_id = Field('customerID')
    default_approval_process_id = Field('defaultApprovalProcessID')
    default_category_id = Field('defaultCategoryID')
    default_duration_expression = Field('defaultDurationExpression')
    default_duration_minutes = Field('defaultDurationMinutes')
    default_duration_unit = Field('defaultDurationUnit')
    default_route_id = Field('defaultRouteID')
    ext_ref_id = Field('extRefID')
    has_queue_topics = Field('hasQueueTopics')
    is_public = Field('isPublic')
    project_id = Field('projectID')
    requestor_core_action = Field('requestorCoreAction')
    requestor_forbidden_actions = Field('requestorForbiddenActions')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    template_id = Field('templateID')
    visible_op_task_fields = Field('visibleOpTaskFields')
    customer = Reference('customer')
    default_approval_process = Reference('defaultApprovalProcess')
    default_category = Reference('defaultCategory')
    default_route = Reference('defaultRoute')
    project = Reference('project')
    template = Reference('template')
    queue_topics = Collection('queueTopics')

api.register(QueueDef)


class QueueTopic(Object):
    code = 'QUET'
    allowed_op_task_types = Field('allowedOpTaskTypes')
    customer_id = Field('customerID')
    default_approval_process_id = Field('defaultApprovalProcessID')
    default_category_id = Field('defaultCategoryID')
    default_duration = Field('defaultDuration')
    default_duration_expression = Field('defaultDurationExpression')
    default_duration_minutes = Field('defaultDurationMinutes')
    default_duration_unit = Field('defaultDurationUnit')
    default_route_id = Field('defaultRouteID')
    description = Field('description')
    ext_ref_id = Field('extRefID')
    indented_name = Field('indentedName')
    name = Field('name')
    parent_topic_id = Field('parentTopicID')
    queue_def_id = Field('queueDefID')
    customer = Reference('customer')
    default_approval_process = Reference('defaultApprovalProcess')
    default_category = Reference('defaultCategory')
    default_route = Reference('defaultRoute')
    parent_topic = Reference('parentTopic')
    queue_def = Reference('queueDef')

api.register(QueueTopic)


class Rate(Object):
    code = 'RATE'
    company_id = Field('companyID')
    customer_id = Field('customerID')
    ext_ref_id = Field('extRefID')
    project_id = Field('projectID')
    rate_value = Field('rateValue')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    company = Reference('company')
    customer = Reference('customer')
    project = Reference('project')
    role = Reference('role')

api.register(Rate)


class ReservedTime(Object):
    code = 'RESVT'
    customer_id = Field('customerID')
    end_date = Field('endDate')
    start_date = Field('startDate')
    task_id = Field('taskID')
    user_id = Field('userID')
    customer = Reference('customer')
    task = Reference('task')
    user = Reference('user')

api.register(ReservedTime)


class ResourceAllocation(Object):
    code = 'RSALLO'
    allocation_date = Field('allocationDate')
    budgeted_hours = Field('budgetedHours')
    customer_id = Field('customerID')
    is_split = Field('isSplit')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    project_id = Field('projectID')
    resource_pool_id = Field('resourcePoolID')
    role_id = Field('roleID')
    scheduled_hours = Field('scheduledHours')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    customer = Reference('customer')
    project = Reference('project')
    resource_pool = Reference('resourcePool')
    role = Reference('role')

api.register(ResourceAllocation)


class ResourcePool(Object):
    code = 'RSPOOL'
    customer_id = Field('customerID')
    description = Field('description')
    display_order = Field('displayOrder')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    customer = Reference('customer')
    resource_allocations = Collection('resourceAllocations')
    roles = Collection('roles')
    users = Collection('users')

api.register(ResourcePool)


class Risk(Object):
    code = 'RISK'
    actual_cost = Field('actualCost')
    customer_id = Field('customerID')
    description = Field('description')
    estimated_effect = Field('estimatedEffect')
    ext_ref_id = Field('extRefID')
    mitigation_cost = Field('mitigationCost')
    mitigation_description = Field('mitigationDescription')
    probability = Field('probability')
    project_id = Field('projectID')
    risk_type_id = Field('riskTypeID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    status = Field('status')
    template_id = Field('templateID')
    customer = Reference('customer')
    project = Reference('project')
    risk_type = Reference('riskType')
    template = Reference('template')

api.register(Risk)


class RiskType(Object):
    code = 'RSKTYP'
    customer_id = Field('customerID')
    description = Field('description')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    customer = Reference('customer')

api.register(RiskType)


class Role(Object):
    code = 'ROLE'
    billing_per_hour = Field('billingPerHour')
    cost_per_hour = Field('costPerHour')
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    layout_template_id = Field('layoutTemplateID')
    max_users = Field('maxUsers')
    name = Field('name')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    layout_template = Reference('layoutTemplate')

api.register(Role)


class RoutingRule(Object):
    code = 'RRUL'
    customer_id = Field('customerID')
    default_assigned_to_id = Field('defaultAssignedToID')
    default_project_id = Field('defaultProjectID')
    default_role_id = Field('defaultRoleID')
    default_team_id = Field('defaultTeamID')
    description = Field('description')
    name = Field('name')
    project_id = Field('projectID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    template_id = Field('templateID')
    customer = Reference('customer')
    default_assigned_to = Reference('defaultAssignedTo')
    default_project = Reference('defaultProject')
    default_role = Reference('defaultRole')
    default_team = Reference('defaultTeam')
    project = Reference('project')
    template = Reference('template')

api.register(RoutingRule)


class Schedule(Object):
    code = 'SCHED'
    customer_id = Field('customerID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    friday = Field('friday')
    group_id = Field('groupID')
    has_non_work_days = Field('hasNonWorkDays')
    is_default = Field('isDefault')
    monday = Field('monday')
    name = Field('name')
    saturday = Field('saturday')
    sunday = Field('sunday')
    thursday = Field('thursday')
    time_zone = Field('timeZone')
    tuesday = Field('tuesday')
    wednesday = Field('wednesday')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    group = Reference('group')
    non_work_days = Collection('nonWorkDays')
    other_groups = Collection('otherGroups')

    def get_earliest_work_time_of_day(self, date=None):
        """
        The ``getEarliestWorkTimeOfDay`` action.
        
        :param date: date (type: ``dateTime``)
        :return: ``dateTime``
        """
        params = {}
        if date is not None: params['date'] = date
        data = self.session.put(self.api_url()+'/getEarliestWorkTimeOfDay', params)
        return data['result']

    def get_latest_work_time_of_day(self, date=None):
        """
        The ``getLatestWorkTimeOfDay`` action.
        
        :param date: date (type: ``dateTime``)
        :return: ``dateTime``
        """
        params = {}
        if date is not None: params['date'] = date
        data = self.session.put(self.api_url()+'/getLatestWorkTimeOfDay', params)
        return data['result']

    def get_next_completion_date(self, date=None, cost_in_minutes=None):
        """
        The ``getNextCompletionDate`` action.
        
        :param date: date (type: ``dateTime``)
        :param cost_in_minutes: costInMinutes (type: ``int``)
        :return: ``dateTime``
        """
        params = {}
        if date is not None: params['date'] = date
        if cost_in_minutes is not None: params['costInMinutes'] = cost_in_minutes
        data = self.session.put(self.api_url()+'/getNextCompletionDate', params)
        return data['result']

    def get_next_start_date(self, date=None):
        """
        The ``getNextStartDate`` action.
        
        :param date: date (type: ``dateTime``)
        :return: ``dateTime``
        """
        params = {}
        if date is not None: params['date'] = date
        data = self.session.put(self.api_url()+'/getNextStartDate', params)
        return data['result']

api.register(Schedule)


class ScoreCard(Object):
    code = 'SCORE'
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    is_public = Field('isPublic')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    project_id = Field('projectID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    template_id = Field('templateID')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    project = Reference('project')
    template = Reference('template')
    score_card_questions = Collection('scoreCardQuestions')

api.register(ScoreCard)


class ScoreCardAnswer(Object):
    code = 'SCANS'
    customer_id = Field('customerID')
    number_val = Field('numberVal')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    project_id = Field('projectID')
    score_card_id = Field('scoreCardID')
    score_card_option_id = Field('scoreCardOptionID')
    score_card_question_id = Field('scoreCardQuestionID')
    template_id = Field('templateID')
    type = Field('type')
    customer = Reference('customer')
    project = Reference('project')
    score_card = Reference('scoreCard')
    score_card_option = Reference('scoreCardOption')
    score_card_question = Reference('scoreCardQuestion')
    template = Reference('template')

api.register(ScoreCardAnswer)


class ScoreCardOption(Object):
    code = 'SCOPT'
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    is_default = Field('isDefault')
    is_hidden = Field('isHidden')
    label = Field('label')
    score_card_question_id = Field('scoreCardQuestionID')
    value = Field('value')
    customer = Reference('customer')
    score_card_question = Reference('scoreCardQuestion')

api.register(ScoreCardOption)


class ScoreCardQuestion(Object):
    code = 'SCOREQ'
    customer_id = Field('customerID')
    description = Field('description')
    display_order = Field('displayOrder')
    display_type = Field('displayType')
    name = Field('name')
    score_card_id = Field('scoreCardID')
    weight = Field('weight')
    customer = Reference('customer')
    score_card = Reference('scoreCard')
    score_card_options = Collection('scoreCardOptions')

api.register(ScoreCardQuestion)


class StepApprover(Object):
    code = 'SPAPVR'
    approval_step_id = Field('approvalStepID')
    customer_id = Field('customerID')
    role_id = Field('roleID')
    team_id = Field('teamID')
    user_id = Field('userID')
    wild_card = Field('wildCard')
    approval_step = Reference('approvalStep')
    customer = Reference('customer')
    role = Reference('role')
    team = Reference('team')
    user = Reference('user')

api.register(StepApprover)


class Task(Object):
    code = 'TASK'
    url = Field('URL')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration = Field('actualDuration')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_expense_cost = Field('actualExpenseCost')
    actual_labor_cost = Field('actualLaborCost')
    actual_revenue = Field('actualRevenue')
    actual_start_date = Field('actualStartDate')
    actual_work = Field('actualWork')
    actual_work_required = Field('actualWorkRequired')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    assigned_to_id = Field('assignedToID')
    assignments_list_string = Field('assignmentsListString')
    audit_note = Field('auditNote')
    audit_types = Field('auditTypes')
    audit_user_ids = Field('auditUserIDs')
    backlog_order = Field('backlogOrder')
    billing_amount = Field('billingAmount')
    billing_record_id = Field('billingRecordID')
    can_start = Field('canStart')
    category_id = Field('categoryID')
    color = Field('color')
    commit_date = Field('commitDate')
    commit_date_range = Field('commitDateRange')
    completion_pending_date = Field('completionPendingDate')
    condition = Field('condition')
    constraint_date = Field('constraintDate')
    converted_op_task_entry_date = Field('convertedOpTaskEntryDate')
    converted_op_task_name = Field('convertedOpTaskName')
    converted_op_task_originator_id = Field('convertedOpTaskOriginatorID')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    cpi = Field('cpi')
    csi = Field('csi')
    current_approval_step_id = Field('currentApprovalStepID')
    customer_id = Field('customerID')
    days_late = Field('daysLate')
    description = Field('description')
    due_date = Field('dueDate')
    duration = Field('duration')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    eac = Field('eac')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    estimate = Field('estimate')
    ext_ref_id = Field('extRefID')
    group_id = Field('groupID')
    handoff_date = Field('handoffDate')
    has_completion_constraint = Field('hasCompletionConstraint')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_resolvables = Field('hasResolvables')
    has_start_constraint = Field('hasStartConstraint')
    has_timed_notifications = Field('hasTimedNotifications')
    hours_per_point = Field('hoursPerPoint')
    indent = Field('indent')
    is_agile = Field('isAgile')
    is_critical = Field('isCritical')
    is_duration_locked = Field('isDurationLocked')
    is_leveling_excluded = Field('isLevelingExcluded')
    is_ready = Field('isReady')
    is_work_required_locked = Field('isWorkRequiredLocked')
    iteration_id = Field('iterationID')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_start_delay = Field('levelingStartDelay')
    leveling_start_delay_expression = Field('levelingStartDelayExpression')
    leveling_start_delay_minutes = Field('levelingStartDelayMinutes')
    master_task_id = Field('masterTaskID')
    milestone_id = Field('milestoneID')
    name = Field('name')
    number_of_children = Field('numberOfChildren')
    number_open_op_tasks = Field('numberOpenOpTasks')
    original_duration = Field('originalDuration')
    original_work_required = Field('originalWorkRequired')
    parent_id = Field('parentID')
    parent_lag = Field('parentLag')
    parent_lag_type = Field('parentLagType')
    percent_complete = Field('percentComplete')
    personal = Field('personal')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_duration = Field('plannedDuration')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_start_date = Field('plannedStartDate')
    predecessor_expression = Field('predecessorExpression')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    progress_status = Field('progressStatus')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_duration_minutes = Field('projectedDurationMinutes')
    projected_start_date = Field('projectedStartDate')
    recurrence_number = Field('recurrenceNumber')
    recurrence_rule_id = Field('recurrenceRuleID')
    reference_number = Field('referenceNumber')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_duration_minutes = Field('remainingDurationMinutes')
    reserved_time_id = Field('reservedTimeID')
    resource_scope = Field('resourceScope')
    revenue_type = Field('revenueType')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    slack_date = Field('slackDate')
    spi = Field('spi')
    status = Field('status')
    status_equates_with = Field('statusEquatesWith')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    task_constraint = Field('taskConstraint')
    task_number = Field('taskNumber')
    task_number_predecessor_string = Field('taskNumberPredecessorString')
    team_id = Field('teamID')
    template_task_id = Field('templateTaskID')
    tracking_mode = Field('trackingMode')
    wbs = Field('wbs')
    work = Field('work')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    work_unit = Field('workUnit')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    billing_record = Reference('billingRecord')
    category = Reference('category')
    converted_op_task_originator = Reference('convertedOpTaskOriginator')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    default_baseline_task = Reference('defaultBaselineTask')
    entered_by = Reference('enteredBy')
    group = Reference('group')
    iteration = Reference('iteration')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone = Reference('milestone')
    parent = Reference('parent')
    primary_assignment = Reference('primaryAssignment')
    project = Reference('project')
    rejection_issue = Reference('rejectionIssue')
    reserved_time = Reference('reservedTime')
    role = Reference('role')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    template_task = Reference('templateTask')
    work_item = Reference('workItem')
    access_rules = Collection('accessRules')
    all_priorities = Collection('allPriorities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    assignments = Collection('assignments')
    children = Collection('children')
    documents = Collection('documents')
    done_statuses = Collection('doneStatuses')
    expenses = Collection('expenses')
    hours = Collection('hours')
    op_tasks = Collection('opTasks')
    open_op_tasks = Collection('openOpTasks')
    predecessors = Collection('predecessors')
    resolvables = Collection('resolvables')
    successors = Collection('successors')
    updates = Collection('updates')

    def accept_work(self):
        """
        The ``acceptWork`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/acceptWork', params)
        

    def approve_approval(self, user_id=None, username=None, password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``approveApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/approveApproval', params)
        

    def assign(self, obj_id=None, obj_code=None):
        """
        The ``assign`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        data = self.session.put(self.api_url()+'/assign', params)
        

    def bulk_copy(self, task_ids=None, project_id=None, parent_id=None, options=None):
        """
        The ``bulkCopy`` action.
        
        :param task_ids: taskIDs (type: ``string[]``)
        :param project_id: projectID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if task_ids is not None: params['taskIDs'] = task_ids
        if project_id is not None: params['projectID'] = project_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/bulkCopy', params)
        return data['result']

    def bulk_move(self, task_ids=None, project_id=None, parent_id=None, options=None):
        """
        The ``bulkMove`` action.
        
        :param task_ids: taskIDs (type: ``string[]``)
        :param project_id: projectID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        """
        params = {}
        if task_ids is not None: params['taskIDs'] = task_ids
        if project_id is not None: params['projectID'] = project_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/bulkMove', params)
        

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def mark_done(self, status=None):
        """
        The ``markDone`` action.
        
        :param status: status (type: ``string``)
        """
        params = {}
        if status is not None: params['status'] = status
        data = self.session.put(self.api_url()+'/markDone', params)
        

    def mark_not_done(self, assignment_id=None):
        """
        The ``markNotDone`` action.
        
        :param assignment_id: assignmentID (type: ``string``)
        """
        params = {}
        if assignment_id is not None: params['assignmentID'] = assignment_id
        data = self.session.put(self.api_url()+'/markNotDone', params)
        

    def move(self, project_id=None, parent_id=None, options=None):
        """
        The ``move`` action.
        
        :param project_id: projectID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        """
        params = {}
        if project_id is not None: params['projectID'] = project_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/move', params)
        

    def recall_approval(self):
        """
        The ``recallApproval`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/recallApproval', params)
        

    def reject_approval(self, user_id=None, username=None, password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``rejectApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/rejectApproval', params)
        

    def reply_to_assignment(self, note_text=None, commit_date=None):
        """
        The ``replyToAssignment`` action.
        
        :param note_text: noteText (type: ``string``)
        :param commit_date: commitDate (type: ``dateTime``)
        """
        params = {}
        if note_text is not None: params['noteText'] = note_text
        if commit_date is not None: params['commitDate'] = commit_date
        data = self.session.put(self.api_url()+'/replyToAssignment', params)
        

    def unaccept_work(self):
        """
        The ``unacceptWork`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unacceptWork', params)
        

    def unassign(self, user_id=None):
        """
        The ``unassign`` action.
        
        :param user_id: userID (type: ``string``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/unassign', params)
        

    def unassign_occurrences(self, user_id=None):
        """
        The ``unassignOccurrences`` action.
        
        :param user_id: userID (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/unassignOccurrences', params)
        return data['result']

    def add_comment(self, text):
        """
        Add a comment to the current object containing the supplied text.

        The new :class:`Comment` instance is returned, it does not need to be
        saved.
        """

        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.code,
            obj_id = self.id
        )
        comment.save()
        return comment

api.register(Task)


class Team(Object):
    code = 'TEAMOB'
    customer_id = Field('customerID')
    description = Field('description')
    estimate_by_hours = Field('estimateByHours')
    hours_per_point = Field('hoursPerPoint')
    is_agile = Field('isAgile')
    is_standard_issue_list = Field('isStandardIssueList')
    layout_template_id = Field('layoutTemplateID')
    my_work_view_id = Field('myWorkViewID')
    name = Field('name')
    op_task_bug_report_statuses = Field('opTaskBugReportStatuses')
    op_task_change_order_statuses = Field('opTaskChangeOrderStatuses')
    op_task_issue_statuses = Field('opTaskIssueStatuses')
    op_task_request_statuses = Field('opTaskRequestStatuses')
    owner_id = Field('ownerID')
    requests_view_id = Field('requestsViewID')
    task_statuses = Field('taskStatuses')
    team_story_board_statuses = Field('teamStoryBoardStatuses')
    customer = Reference('customer')
    layout_template = Reference('layoutTemplate')
    my_work_view = Reference('myWorkView')
    owner = Reference('owner')
    requests_view = Reference('requestsView')
    backlog_tasks = Collection('backlogTasks')
    team_members = Collection('teamMembers')
    updates = Collection('updates')
    users = Collection('users')

api.register(Team)


class TeamMember(Object):
    code = 'TEAMMB'
    customer_id = Field('customerID')
    has_assign_permissions = Field('hasAssignPermissions')
    team_id = Field('teamID')
    user_id = Field('userID')
    customer = Reference('customer')
    team = Reference('team')
    user = Reference('user')

api.register(TeamMember)


class Template(Object):
    code = 'TMPL'
    approval_process_id = Field('approvalProcessID')
    auto_baseline_recur_on = Field('autoBaselineRecurOn')
    auto_baseline_recurrence_type = Field('autoBaselineRecurrenceType')
    category_id = Field('categoryID')
    completion_day = Field('completionDay')
    completion_type = Field('completionType')
    currency = Field('currency')
    customer_id = Field('customerID')
    deliverable_score_card_id = Field('deliverableScoreCardID')
    deliverable_success_score = Field('deliverableSuccessScore')
    description = Field('description')
    duration_minutes = Field('durationMinutes')
    enable_auto_baselines = Field('enableAutoBaselines')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    filter_hour_types = Field('filterHourTypes')
    fixed_cost = Field('fixedCost')
    fixed_revenue = Field('fixedRevenue')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_notes = Field('hasNotes')
    has_timed_notifications = Field('hasTimedNotifications')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    milestone_path_id = Field('milestonePathID')
    name = Field('name')
    olv = Field('olv')
    owner_privileges = Field('ownerPrivileges')
    performance_index_method = Field('performanceIndexMethod')
    planned_cost = Field('plannedCost')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_risk_cost = Field('plannedRiskCost')
    queue_def_id = Field('queueDefID')
    reference_number = Field('referenceNumber')
    schedule_mode = Field('scheduleMode')
    start_day = Field('startDay')
    summary_completion_type = Field('summaryCompletionType')
    version = Field('version')
    work_required = Field('workRequired')
    approval_process = Reference('approvalProcess')
    category = Reference('category')
    customer = Reference('customer')
    deliverable_score_card = Reference('deliverableScoreCard')
    entered_by = Reference('enteredBy')
    exchange_rate = Reference('exchangeRate')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone_path = Reference('milestonePath')
    queue_def = Reference('queueDef')
    access_rules = Collection('accessRules')
    deliverable_values = Collection('deliverableValues')
    documents = Collection('documents')
    expenses = Collection('expenses')
    groups = Collection('groups')
    hour_types = Collection('hourTypes')
    risks = Collection('risks')
    roles = Collection('roles')
    routing_rules = Collection('routingRules')
    template_tasks = Collection('templateTasks')
    template_user_roles = Collection('templateUserRoles')
    template_users = Collection('templateUsers')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

api.register(Template)


class TemplateAssignment(Object):
    code = 'TASSGN'
    assigned_to_id = Field('assignedToID')
    assignment_percent = Field('assignmentPercent')
    customer_id = Field('customerID')
    is_primary = Field('isPrimary')
    is_team_assignment = Field('isTeamAssignment')
    master_task_id = Field('masterTaskID')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    role_id = Field('roleID')
    team_id = Field('teamID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    work_required = Field('workRequired')
    work_unit = Field('workUnit')
    assigned_to = Reference('assignedTo')
    customer = Reference('customer')
    role = Reference('role')
    team = Reference('team')
    template = Reference('template')
    template_task = Reference('templateTask')

api.register(TemplateAssignment)


class TemplatePredecessor(Object):
    code = 'TPRED'
    customer_id = Field('customerID')
    is_enforced = Field('isEnforced')
    lag_days = Field('lagDays')
    lag_type = Field('lagType')
    predecessor_id = Field('predecessorID')
    predecessor_type = Field('predecessorType')
    successor_id = Field('successorID')
    customer = Reference('customer')
    predecessor = Reference('predecessor')
    successor = Reference('successor')

api.register(TemplatePredecessor)


class TemplateTask(Object):
    code = 'TTSK'
    url = Field('URL')
    approval_process_id = Field('approvalProcessID')
    assigned_to_id = Field('assignedToID')
    audit_types = Field('auditTypes')
    billing_amount = Field('billingAmount')
    category_id = Field('categoryID')
    completion_day = Field('completionDay')
    constraint_day = Field('constraintDay')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    customer_id = Field('customerID')
    description = Field('description')
    duration = Field('duration')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_notes = Field('hasNotes')
    has_timed_notifications = Field('hasTimedNotifications')
    indent = Field('indent')
    is_critical = Field('isCritical')
    is_duration_locked = Field('isDurationLocked')
    is_leveling_excluded = Field('isLevelingExcluded')
    is_work_required_locked = Field('isWorkRequiredLocked')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_start_delay = Field('levelingStartDelay')
    leveling_start_delay_minutes = Field('levelingStartDelayMinutes')
    master_task_id = Field('masterTaskID')
    milestone_id = Field('milestoneID')
    name = Field('name')
    number_of_children = Field('numberOfChildren')
    original_duration = Field('originalDuration')
    original_work_required = Field('originalWorkRequired')
    parent_id = Field('parentID')
    parent_lag = Field('parentLag')
    parent_lag_type = Field('parentLagType')
    planned_cost = Field('plannedCost')
    planned_duration = Field('plannedDuration')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    priority = Field('priority')
    recurrence_number = Field('recurrenceNumber')
    recurrence_rule_id = Field('recurrenceRuleID')
    reference_number = Field('referenceNumber')
    revenue_type = Field('revenueType')
    role_id = Field('roleID')
    start_day = Field('startDay')
    task_constraint = Field('taskConstraint')
    task_number = Field('taskNumber')
    team_id = Field('teamID')
    template_id = Field('templateID')
    tracking_mode = Field('trackingMode')
    work = Field('work')
    work_required = Field('workRequired')
    work_unit = Field('workUnit')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone = Reference('milestone')
    parent = Reference('parent')
    role = Reference('role')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    template = Reference('template')
    assignments = Collection('assignments')
    children = Collection('children')
    documents = Collection('documents')
    expenses = Collection('expenses')
    predecessors = Collection('predecessors')
    successors = Collection('successors')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def move(self, template_id=None, parent_id=None, options=None):
        """
        The ``move`` action.
        
        :param template_id: templateID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        """
        params = {}
        if template_id is not None: params['templateID'] = template_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/move', params)
        

api.register(TemplateTask)


class TemplateUser(Object):
    code = 'TMTU'
    customer_id = Field('customerID')
    template_id = Field('templateID')
    tmp_user_id = Field('tmpUserID')
    user_id = Field('userID')
    customer = Reference('customer')
    template = Reference('template')
    user = Reference('user')

api.register(TemplateUser)


class TemplateUserRole(Object):
    code = 'TTEAM'
    customer_id = Field('customerID')
    role_id = Field('roleID')
    template_id = Field('templateID')
    user_id = Field('userID')
    customer = Reference('customer')
    role = Reference('role')
    template = Reference('template')
    user = Reference('user')

api.register(TemplateUserRole)


class Timesheet(Object):
    code = 'TSHET'
    approver_id = Field('approverID')
    available_actions = Field('availableActions')
    customer_id = Field('customerID')
    display_name = Field('displayName')
    end_date = Field('endDate')
    ext_ref_id = Field('extRefID')
    has_notes = Field('hasNotes')
    hours_duration = Field('hoursDuration')
    is_editable = Field('isEditable')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    overtime_hours = Field('overtimeHours')
    regular_hours = Field('regularHours')
    start_date = Field('startDate')
    status = Field('status')
    timesheet_profile_id = Field('timesheetProfileID')
    total_hours = Field('totalHours')
    user_id = Field('userID')
    approver = Reference('approver')
    customer = Reference('customer')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    user = Reference('user')
    hours = Collection('hours')

api.register(Timesheet)


class UIFilter(Object):
    code = 'UIFT'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    definition = Field('definition')
    display_name = Field('displayName')
    entered_by_id = Field('enteredByID')
    filter_type = Field('filterType')
    global_uikey = Field('globalUIKey')
    is_app_global_editable = Field('isAppGlobalEditable')
    is_public = Field('isPublic')
    is_report = Field('isReport')
    is_saved_search = Field('isSavedSearch')
    is_text = Field('isText')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    mod_date = Field('modDate')
    msg_key = Field('msgKey')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    preference_id = Field('preferenceID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    ui_obj_code = Field('uiObjCode')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    access_rules = Collection('accessRules')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')
    users = Collection('users')

api.register(UIFilter)


class UIGroupBy(Object):
    code = 'UIGB'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    definition = Field('definition')
    display_name = Field('displayName')
    entered_by_id = Field('enteredByID')
    global_uikey = Field('globalUIKey')
    is_app_global_editable = Field('isAppGlobalEditable')
    is_public = Field('isPublic')
    is_report = Field('isReport')
    is_text = Field('isText')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    mod_date = Field('modDate')
    msg_key = Field('msgKey')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    preference_id = Field('preferenceID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    ui_obj_code = Field('uiObjCode')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    access_rules = Collection('accessRules')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')

api.register(UIGroupBy)


class UIView(Object):
    code = 'UIVW'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    definition = Field('definition')
    display_name = Field('displayName')
    entered_by_id = Field('enteredByID')
    global_uikey = Field('globalUIKey')
    is_app_global_editable = Field('isAppGlobalEditable')
    is_default = Field('isDefault')
    is_new_format = Field('isNewFormat')
    is_public = Field('isPublic')
    is_report = Field('isReport')
    is_text = Field('isText')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    layout_type = Field('layoutType')
    mod_date = Field('modDate')
    msg_key = Field('msgKey')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    preference_id = Field('preferenceID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    ui_obj_code = Field('uiObjCode')
    uiview_type = Field('uiviewType')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    access_rules = Collection('accessRules')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')

api.register(UIView)


class Update(Object):
    code = 'UPDATE'
    allowed_actions = Field('allowedActions')
    entered_by_id = Field('enteredByID')
    entered_by_name = Field('enteredByName')
    entry_date = Field('entryDate')
    icon_name = Field('iconName')
    icon_path = Field('iconPath')
    message = Field('message')
    ref_name = Field('refName')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    styled_message = Field('styledMessage')
    sub_message = Field('subMessage')
    sub_obj_code = Field('subObjCode')
    sub_obj_id = Field('subObjID')
    thread_id = Field('threadID')
    top_name = Field('topName')
    top_obj_code = Field('topObjCode')
    top_obj_id = Field('topObjID')
    update_actions = Field('updateActions')
    update_obj_code = Field('updateObjCode')
    update_obj_id = Field('updateObjID')
    update_type = Field('updateType')
    update_journal_entry = Reference('updateJournalEntry')
    update_note = Reference('updateNote')
    combined_updates = Collection('combinedUpdates')
    message_args = Collection('messageArgs')
    nested_updates = Collection('nestedUpdates')
    replies = Collection('replies')
    sub_message_args = Collection('subMessageArgs')

    @property
    def update_obj(self):
        """
        The object referenced by this update.
        """
        return self.session.api.from_data(
            self.session, dict(
                ID=self.update_obj_id,
                objCode=self.update_obj_code
            ))

api.register(Update)


class User(Object):
    code = 'USER'
    access_level_id = Field('accessLevelID')
    address = Field('address')
    address2 = Field('address2')
    avatar_date = Field('avatarDate')
    avatar_download_url = Field('avatarDownloadURL')
    avatar_size = Field('avatarSize')
    avatar_x = Field('avatarX')
    avatar_y = Field('avatarY')
    billing_per_hour = Field('billingPerHour')
    category_id = Field('categoryID')
    city = Field('city')
    company_id = Field('companyID')
    cost_per_hour = Field('costPerHour')
    country = Field('country')
    customer_id = Field('customerID')
    default_hour_type_id = Field('defaultHourTypeID')
    default_interface = Field('defaultInterface')
    email_addr = Field('emailAddr')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    first_name = Field('firstName')
    fte = Field('fte')
    has_apiaccess = Field('hasAPIAccess')
    has_documents = Field('hasDocuments')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_password = Field('hasPassword')
    has_proof_license = Field('hasProofLicense')
    has_reserved_times = Field('hasReservedTimes')
    home_group_id = Field('homeGroupID')
    home_team_id = Field('homeTeamID')
    is_active = Field('isActive')
    is_admin = Field('isAdmin')
    is_box_authenticated = Field('isBoxAuthenticated')
    is_drop_box_authenticated = Field('isDropBoxAuthenticated')
    is_google_authenticated = Field('isGoogleAuthenticated')
    is_share_point_authenticated = Field('isSharePointAuthenticated')
    is_web_damauthenticated = Field('isWebDAMAuthenticated')
    last_announcement = Field('lastAnnouncement')
    last_entered_note_id = Field('lastEnteredNoteID')
    last_login_date = Field('lastLoginDate')
    last_name = Field('lastName')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    last_whats_new = Field('lastWhatsNew')
    latest_update_note_id = Field('latestUpdateNoteID')
    layout_template_id = Field('layoutTemplateID')
    license_type = Field('licenseType')
    locale = Field('locale')
    login_count = Field('loginCount')
    manager_id = Field('managerID')
    mobile_phone_number = Field('mobilePhoneNumber')
    my_info = Field('myInfo')
    name = Field('name')
    password = Field('password')
    password_date = Field('passwordDate')
    persona = Field('persona')
    phone_extension = Field('phoneExtension')
    phone_number = Field('phoneNumber')
    portal_profile_id = Field('portalProfileID')
    postal_code = Field('postalCode')
    proof_account_password = Field('proofAccountPassword')
    registration_expire_date = Field('registrationExpireDate')
    reset_password_expire_date = Field('resetPasswordExpireDate')
    resource_pool_id = Field('resourcePoolID')
    role_id = Field('roleID')
    schedule_id = Field('scheduleID')
    sso_access_only = Field('ssoAccessOnly')
    sso_username = Field('ssoUsername')
    state = Field('state')
    status_update = Field('statusUpdate')
    time_zone = Field('timeZone')
    timesheet_profile_id = Field('timesheetProfileID')
    title = Field('title')
    username = Field('username')
    web_davprofile = Field('webDAVProfile')
    category = Reference('category')
    company = Reference('company')
    customer = Reference('customer')
    default_hour_type = Reference('defaultHourType')
    entered_by = Reference('enteredBy')
    high_priority_work_item = Reference('highPriorityWorkItem')
    home_group = Reference('homeGroup')
    home_team = Reference('homeTeam')
    last_entered_note = Reference('lastEnteredNote')
    last_note = Reference('lastNote')
    last_status_note = Reference('lastStatusNote')
    last_updated_by = Reference('lastUpdatedBy')
    latest_update_note = Reference('latestUpdateNote')
    layout_template = Reference('layoutTemplate')
    manager = Reference('manager')
    resource_pool = Reference('resourcePool')
    role = Reference('role')
    schedule = Reference('schedule')
    direct_reports = Collection('directReports')
    documents = Collection('documents')
    favorites = Collection('favorites')
    hour_types = Collection('hourTypes')
    messages = Collection('messages')
    other_groups = Collection('otherGroups')
    reserved_times = Collection('reservedTimes')
    roles = Collection('roles')
    teams = Collection('teams')
    ui_filters = Collection('uiFilters')
    ui_group_bys = Collection('uiGroupBys')
    ui_views = Collection('uiViews')
    updates = Collection('updates')
    user_activities = Collection('userActivities')
    user_notes = Collection('userNotes')
    user_pref_values = Collection('userPrefValues')
    work_items = Collection('workItems')

    def assign_user_token(self):
        """
        The ``assignUserToken`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/assignUserToken', params)
        return data['result']

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def complete_user_registration(self, first_name=None, last_name=None, token=None, title=None, new_password=None):
        """
        The ``completeUserRegistration`` action.
        
        :param first_name: firstName (type: ``string``)
        :param last_name: lastName (type: ``string``)
        :param token: token (type: ``string``)
        :param title: title (type: ``string``)
        :param new_password: newPassword (type: ``string``)
        """
        params = {}
        if first_name is not None: params['firstName'] = first_name
        if last_name is not None: params['lastName'] = last_name
        if token is not None: params['token'] = token
        if title is not None: params['title'] = title
        if new_password is not None: params['newPassword'] = new_password
        data = self.session.put(self.api_url()+'/completeUserRegistration', params)
        

    def send_invitation_email(self):
        """
        The ``sendInvitationEmail`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/sendInvitationEmail', params)
        

api.register(User)


class UserActivity(Object):
    code = 'USERAC'
    customer_id = Field('customerID')
    entry_date = Field('entryDate')
    last_update_date = Field('lastUpdateDate')
    name = Field('name')
    user_id = Field('userID')
    value = Field('value')
    customer = Reference('customer')
    user = Reference('user')

api.register(UserActivity)


class UserNote(Object):
    code = 'USRNOT'
    customer_id = Field('customerID')
    document_approval_id = Field('documentApprovalID')
    document_request_id = Field('documentRequestID')
    document_share_id = Field('documentShareID')
    endorsement_id = Field('endorsementID')
    entry_date = Field('entryDate')
    event_type = Field('eventType')
    journal_entry_id = Field('journalEntryID')
    like_id = Field('likeID')
    note_id = Field('noteID')
    user_id = Field('userID')
    customer = Reference('customer')
    document_approval = Reference('documentApproval')
    journal_entry = Reference('journalEntry')
    note = Reference('note')
    user = Reference('user')

api.register(UserNote)


class UserPrefValue(Object):
    code = 'USERPF'
    customer_id = Field('customerID')
    name = Field('name')
    user_id = Field('userID')
    value = Field('value')
    customer = Reference('customer')
    user = Reference('user')

api.register(UserPrefValue)


class Work(Object):
    code = 'WORK'
    url = Field('URL')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration = Field('actualDuration')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_expense_cost = Field('actualExpenseCost')
    actual_labor_cost = Field('actualLaborCost')
    actual_revenue = Field('actualRevenue')
    actual_start_date = Field('actualStartDate')
    actual_work = Field('actualWork')
    actual_work_required = Field('actualWorkRequired')
    actual_work_required_expression = Field('actualWorkRequiredExpression')
    age_range_as_string = Field('ageRangeAsString')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    assigned_to_id = Field('assignedToID')
    assignments_list_string = Field('assignmentsListString')
    audit_note = Field('auditNote')
    audit_types = Field('auditTypes')
    audit_user_ids = Field('auditUserIDs')
    auto_closure_date = Field('autoClosureDate')
    backlog_order = Field('backlogOrder')
    billing_amount = Field('billingAmount')
    billing_record_id = Field('billingRecordID')
    can_start = Field('canStart')
    category_id = Field('categoryID')
    color = Field('color')
    commit_date = Field('commitDate')
    commit_date_range = Field('commitDateRange')
    completion_pending_date = Field('completionPendingDate')
    condition = Field('condition')
    constraint_date = Field('constraintDate')
    converted_op_task_entry_date = Field('convertedOpTaskEntryDate')
    converted_op_task_name = Field('convertedOpTaskName')
    converted_op_task_originator_id = Field('convertedOpTaskOriginatorID')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    cpi = Field('cpi')
    csi = Field('csi')
    current_approval_step_id = Field('currentApprovalStepID')
    current_status_duration = Field('currentStatusDuration')
    customer_id = Field('customerID')
    days_late = Field('daysLate')
    description = Field('description')
    due_date = Field('dueDate')
    duration = Field('duration')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    eac = Field('eac')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    estimate = Field('estimate')
    ext_ref_id = Field('extRefID')
    first_response = Field('firstResponse')
    group_id = Field('groupID')
    handoff_date = Field('handoffDate')
    has_completion_constraint = Field('hasCompletionConstraint')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_resolvables = Field('hasResolvables')
    has_start_constraint = Field('hasStartConstraint')
    has_timed_notifications = Field('hasTimedNotifications')
    hours_per_point = Field('hoursPerPoint')
    how_old = Field('howOld')
    indent = Field('indent')
    is_agile = Field('isAgile')
    is_complete = Field('isComplete')
    is_critical = Field('isCritical')
    is_duration_locked = Field('isDurationLocked')
    is_help_desk = Field('isHelpDesk')
    is_leveling_excluded = Field('isLevelingExcluded')
    is_ready = Field('isReady')
    is_work_required_locked = Field('isWorkRequiredLocked')
    iteration_id = Field('iterationID')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_start_delay = Field('levelingStartDelay')
    leveling_start_delay_expression = Field('levelingStartDelayExpression')
    leveling_start_delay_minutes = Field('levelingStartDelayMinutes')
    master_task_id = Field('masterTaskID')
    milestone_id = Field('milestoneID')
    name = Field('name')
    number_of_children = Field('numberOfChildren')
    number_open_op_tasks = Field('numberOpenOpTasks')
    op_task_type = Field('opTaskType')
    op_task_type_label = Field('opTaskTypeLabel')
    original_duration = Field('originalDuration')
    original_work_required = Field('originalWorkRequired')
    owner_id = Field('ownerID')
    parent_id = Field('parentID')
    parent_lag = Field('parentLag')
    parent_lag_type = Field('parentLagType')
    percent_complete = Field('percentComplete')
    personal = Field('personal')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_duration = Field('plannedDuration')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_start_date = Field('plannedStartDate')
    predecessor_expression = Field('predecessorExpression')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    progress_status = Field('progressStatus')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_duration_minutes = Field('projectedDurationMinutes')
    projected_start_date = Field('projectedStartDate')
    queue_topic_id = Field('queueTopicID')
    recurrence_number = Field('recurrenceNumber')
    recurrence_rule_id = Field('recurrenceRuleID')
    reference_number = Field('referenceNumber')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_duration_minutes = Field('remainingDurationMinutes')
    reserved_time_id = Field('reservedTimeID')
    resolution_time = Field('resolutionTime')
    resolve_op_task_id = Field('resolveOpTaskID')
    resolve_project_id = Field('resolveProjectID')
    resolve_task_id = Field('resolveTaskID')
    resolving_obj_code = Field('resolvingObjCode')
    resolving_obj_id = Field('resolvingObjID')
    resource_scope = Field('resourceScope')
    revenue_type = Field('revenueType')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    severity = Field('severity')
    slack_date = Field('slackDate')
    source_obj_code = Field('sourceObjCode')
    source_obj_id = Field('sourceObjID')
    source_task_id = Field('sourceTaskID')
    spi = Field('spi')
    status = Field('status')
    status_equates_with = Field('statusEquatesWith')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    task_constraint = Field('taskConstraint')
    task_number = Field('taskNumber')
    task_number_predecessor_string = Field('taskNumberPredecessorString')
    team_id = Field('teamID')
    template_task_id = Field('templateTaskID')
    tracking_mode = Field('trackingMode')
    url_ = Field('url')
    wbs = Field('wbs')
    work = Field('work')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    work_unit = Field('workUnit')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    billing_record = Reference('billingRecord')
    category = Reference('category')
    converted_op_task_originator = Reference('convertedOpTaskOriginator')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    default_baseline_task = Reference('defaultBaselineTask')
    entered_by = Reference('enteredBy')
    group = Reference('group')
    iteration = Reference('iteration')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone = Reference('milestone')
    owner = Reference('owner')
    parent = Reference('parent')
    primary_assignment = Reference('primaryAssignment')
    project = Reference('project')
    queue_topic = Reference('queueTopic')
    rejection_issue = Reference('rejectionIssue')
    reserved_time = Reference('reservedTime')
    resolve_op_task = Reference('resolveOpTask')
    resolve_project = Reference('resolveProject')
    resolve_task = Reference('resolveTask')
    role = Reference('role')
    source_task = Reference('sourceTask')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    template_task = Reference('templateTask')
    work_item = Reference('workItem')
    access_rules = Collection('accessRules')
    all_priorities = Collection('allPriorities')
    all_severities = Collection('allSeverities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    assignments = Collection('assignments')
    children = Collection('children')
    documents = Collection('documents')
    done_statuses = Collection('doneStatuses')
    expenses = Collection('expenses')
    hours = Collection('hours')
    op_tasks = Collection('opTasks')
    open_op_tasks = Collection('openOpTasks')
    predecessors = Collection('predecessors')
    resolvables = Collection('resolvables')
    successors = Collection('successors')
    updates = Collection('updates')

    def team_requests_count(self):
        """
        The ``teamRequestsCount`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/teamRequestsCount', params)
        return data['result']

api.register(Work)


class WorkItem(Object):
    code = 'WRKITM'
    assignment_id = Field('assignmentID')
    customer_id = Field('customerID')
    done_date = Field('doneDate')
    ext_ref_id = Field('extRefID')
    is_dead = Field('isDead')
    is_done = Field('isDone')
    last_viewed_date = Field('lastViewedDate')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    op_task_id = Field('opTaskID')
    priority = Field('priority')
    project_id = Field('projectID')
    reference_object_commit_date = Field('referenceObjectCommitDate')
    reference_object_name = Field('referenceObjectName')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    snooze_date = Field('snoozeDate')
    task_id = Field('taskID')
    user_id = Field('userID')
    assignment = Reference('assignment')
    customer = Reference('customer')
    op_task = Reference('opTask')
    project = Reference('project')
    task = Reference('task')
    user = Reference('user')

    def mark_viewed(self):
        """
        The ``markViewed`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/markViewed', params)
        

api.register(WorkItem)
