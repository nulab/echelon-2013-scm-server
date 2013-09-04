require 'spec_helper'

describe service('supervisord') do
  it { should be_enabled   }
  it { should be_running   }
end
