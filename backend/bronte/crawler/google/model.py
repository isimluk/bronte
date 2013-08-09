#!/usr/bin/python
#
# Copyright (c) 2013 Simon Lukasik
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#

from bronte.crawler.common import CrawlerException

class GoogleLedgerItem(object):
    __fin_base = {
        'balance_sheet': {
                 'Cash & Equivalents',
                 'Short Term Investments',
             'Cash and Short Term Investments',
                 'Accounts Receivable - Trade, Net',
                 'Receivables - Other',
             'Total Receivables, Net',
             'Total Inventory',
             'Prepaid Expenses',
             'Other Current Assets, Total',
             'Total Current Assets',
             'Property/Plant/Equipment, Total - Gross',
             'Accumulated Depreciation, Total',
             'Goodwill, Net',
             'Intangibles, Net',
             'Long Term Investments',
             'Other Long Term Assets, Total',
             'Total Assets',
             'Accounts Payable',
             'Accrued Expenses',
             'Notes Payable/Short Term Debt',
             'Current Port. of LT Debt/Capital Leases',
             'Other Current liabilities, Total',
             'Total Current Liabilities',
                 'Long Term Debt',
                 'Capital Lease Obligations',
             'Total Long Term Debt',
             'Total Debt',
             'Deferred Income Tax',
             'Minority Interest',
             'Other Liabilities, Total',
             'Total Liabilities',
             'Redeemable Preferred Stock, Total',
             'Preferred Stock - Non Redeemable, Net',
             'Common Stock, Total',
             'Additional Paid-In Capital',
             'Retained Earnings (Accumulated Deficit)',
             'Treasury Stock - Common',
             'Other Equity, Total',
             'Total Equity',
             "Total Liabilities & Shareholders' Equity",
                 'Shares Outs - Common Stock Primary Issue',
             'Total Common Shares Outstanding',
             },
        'income_statement': {
            'Revenue',
            'Other Revenue, Total',
            'Total Revenue',
            'Cost of Revenue, Total',
            'Gross Profit',
            'Selling/General/Admin. Expenses, Total',
            'Research & Development',
            'Depreciation/Amortization',
            'Interest Expense(Income) - Net Operating',
            'Unusual Expense (Income)',
            'Other Operating Expenses, Total',
            'Total Operating Expense',
            'Operating Income',
            'Interest Income(Expense), Net Non-Operating',
            'Gain (Loss) on Sale of Assets',
            'Other, Net',
            'Income Before Tax',
            'Income After Tax',
            'Minority Interest',
            'Equity In Affiliates',
            'Net Income Before Extra. Items',
            'Accounting Change',
            'Discontinued Operations',
            'Extraordinary Item',
            'Net Income',
            'Preferred Dividends',
            'Income Available to Common Excl. Extra Items',
            'Income Available to Common Incl. Extra Items',
            'Basic Weighted Average Shares',
            'Basic EPS Excluding Extraordinary Items',
            'Basic EPS Including Extraordinary Items',
            'Dilution Adjustment',
            'Diluted Weighted Average Shares',
            'Diluted EPS Excluding Extraordinary Items',
            'Diluted EPS Including Extraordinary Items',
            'Dividends per Share - Common Stock Primary Issue',
            'Gross Dividends - Common Stock',
            'Net Income after Stock Based Comp. Expense',
            'Basic EPS after Stock Based Comp. Expense',
            'Diluted EPS after Stock Based Comp. Expense',
            'Depreciation, Supplemental',
            'Total Special Items',
            'Normalized Income Before Taxes',
            'Effect of Special Items on Income Taxes',
            'Income Taxes Ex. Impact of Special Items',
            'Normalized Income After Taxes',
            'Normalized Income Avail to Common',
            'Basic Normalized EPS',
            'Diluted Normalized EPS'
             },
        'cash_flow': {
            'Net Income/Starting Line',
            'Depreciation/Depletion',
            'Amortization',
            'Deferred Taxes',
            'Non-Cash Items',
            'Changes in Working Capital',
            'Cash from Operating Activities',
            'Capital Expenditures',
            'Other Investing Cash Flow Items, Total',
            'Cash from Investing Activities',
            'Financing Cash Flow Items',
            'Total Cash Dividends Paid',
            'Issuance (Retirement) of Stock, Net',
            'Issuance (Retirement) of Debt, Net',
            'Cash from Financing Activities',
            'Foreign Exchange Effects',
            'Net Change in Cash',
            'Cash Interest Paid, Supplemental',
            'Cash Taxes Paid, Supplemental'
             }
        }

    @staticmethod
    def get_statement_type(item_name):
        for statement_type, items in GoogleLedgerItem.__fin_base.iteritems():
            if item_name in items:
                return statement_type
        raise CrawlerException("Unrecognized ledger item: %s" % item_name)

