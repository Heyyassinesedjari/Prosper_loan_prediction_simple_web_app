from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, regexp

class StockForm(FlaskForm):
    LoanCurrentDaysDelinquent = DecimalField('', default=0)
    LP_GrossPrincipalLoss = DecimalField('', default=0)
    LoanFirstDefaultedCycleNumber = DecimalField('', default=0)
    LoanMonthsSinceOrigination = DecimalField('', default=0)
    LP_CollectionFees = DecimalField('', default=0)
    EstimatedLoss = DecimalField('', default=0)
    EstimatedReturn = DecimalField('', default=0)
    LP_CustomerPayments = DecimalField('', default=0)
    EstimatedEffectiveYield = DecimalField('', default=0)
    EmploymentStatus = SelectField('Employment Status', choices=[('Self-employed','Self-employed'),('Employed','Employed'),('Not available','Not available'),('Full-time','Full-time'),('Other','Other'),('Not employed','Not employed'),('Part-time','Part-time'),('Retired','Retired')])